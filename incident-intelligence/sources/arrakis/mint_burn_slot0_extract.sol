    function mint(uint256 mintAmount, address receiver)
        external
        nonReentrant
        returns (
            uint256 amount0,
            uint256 amount1,
            uint128 liquidityMinted
        )
    {
        require(mintAmount > 0, "mint 0");
        require(
            restrictedMintToggle != 11111 || msg.sender == _manager,
            "restricted"
        );

        uint256 totalSupply = totalSupply();

        (uint160 sqrtRatioX96, , , , , , ) = pool.slot0();

        if (totalSupply > 0) {
            (uint256 amount0Current, uint256 amount1Current) =
                getUnderlyingBalances();

            amount0 = FullMath.mulDivRoundingUp(
                amount0Current,
                mintAmount,
                totalSupply
            );
            amount1 = FullMath.mulDivRoundingUp(
                amount1Current,
                mintAmount,
                totalSupply
            );
        } else {
            // if supply is 0 mintAmount == liquidity to deposit
            (amount0, amount1) = LiquidityAmounts.getAmountsForLiquidity(
                sqrtRatioX96,
                lowerTick.getSqrtRatioAtTick(),
                upperTick.getSqrtRatioAtTick(),
                SafeCast.toUint128(mintAmount)
            );
        }

        // transfer amounts owed to contract
        if (amount0 > 0) {
            token0.safeTransferFrom(msg.sender, address(this), amount0);
        }
        if (amount1 > 0) {
            token1.safeTransferFrom(msg.sender, address(this), amount1);
        }

        // deposit as much new liquidity as possible
        liquidityMinted = LiquidityAmounts.getLiquidityForAmounts(
            sqrtRatioX96,
            lowerTick.getSqrtRatioAtTick(),
            upperTick.getSqrtRatioAtTick(),
            amount0,
            amount1
        );

        pool.mint(address(this), lowerTick, upperTick, liquidityMinted, "");

        _mint(receiver, mintAmount);
        emit Minted(receiver, mintAmount, amount0, amount1, liquidityMinted);
    }

    /// @notice burn ArrakisVaultV1 Shares (shares of a Uniswap V3 position) and receive underlying
    /// @param burnAmount The number of shares to burn
    /// @param receiver The account to receive the underlying amounts of token0 and token1
    /// @return amount0 amount of token0 transferred to receiver for burning `burnAmount`
    /// @return amount1 amount of token1 transferred to receiver for burning `burnAmount`
    /// @return liquidityBurned amount of liquidity removed from the underlying Uniswap V3 position
    // solhint-disable-next-line function-max-lines
    function burn(uint256 burnAmount, address receiver)
        external
        nonReentrant
        returns (
            uint256 amount0,
            uint256 amount1,
            uint128 liquidityBurned
        )
    {
        require(burnAmount > 0, "burn 0");

        uint256 totalSupply = totalSupply();

        (uint128 liquidity, , , , ) = pool.positions(_getPositionID());

        _burn(msg.sender, burnAmount);

        uint256 liquidityBurned_ =
            FullMath.mulDiv(burnAmount, liquidity, totalSupply);
        liquidityBurned = SafeCast.toUint128(liquidityBurned_);
        (uint256 burn0, uint256 burn1, uint256 fee0, uint256 fee1) =
            _withdraw(lowerTick, upperTick, liquidityBurned);
        _applyFees(fee0, fee1);
        (fee0, fee1) = _subtractAdminFees(fee0, fee1);
        emit FeesEarned(fee0, fee1);

        amount0 =
            burn0 +
            FullMath.mulDiv(
                token0.balanceOf(address(this)) -
                    burn0 -
                    managerBalance0 -
                    arrakisBalance0,
                burnAmount,
                totalSupply
            );
        amount1 =
            burn1 +
            FullMath.mulDiv(
                token1.balanceOf(address(this)) -
                    burn1 -
                    managerBalance1 -
                    arrakisBalance1,
                burnAmount,
                totalSupply
            );

        if (amount0 > 0) {
            token0.safeTransfer(receiver, amount0);
        }

        if (amount1 > 0) {
            token1.safeTransfer(receiver, amount1);
        }

        emit Burned(receiver, burnAmount, amount0, amount1, liquidityBurned);
    }

    // Manager Functions => Called by Pool Manager

    /// @notice Change the range of underlying UniswapV3 position, only manager can call
    /// @dev When changing the range the inventory of token0 and token1 may be rebalanced
    /// with a swap to deposit as much liquidity as possible into the new position. Swap parameters
    /// can be computed by simulating the whole operation: remove all liquidity, deposit as much
    /// as possible into new position, then observe how much of token0 or token1 is leftover.

// ---- _checkSlippage (TWAP, rebalance-only) ----
    function _checkSlippage(uint160 swapThresholdPrice, bool zeroForOne)
        private
        view
    {
        uint32[] memory secondsAgo = new uint32[](2);
        secondsAgo[0] = gelatoSlippageInterval;
        secondsAgo[1] = 0;

        (int56[] memory tickCumulatives, ) = pool.observe(secondsAgo);

        require(tickCumulatives.length == 2, "array len");
        uint160 avgSqrtRatioX96;
        unchecked {
            int24 avgTick =
                int24(
                    (tickCumulatives[1] - tickCumulatives[0]) /
                        int56(uint56(gelatoSlippageInterval))
                );
            avgSqrtRatioX96 = avgTick.getSqrtRatioAtTick();
        }

        uint160 maxSlippage = (avgSqrtRatioX96 * gelatoSlippageBPS) / 10000;
        if (zeroForOne) {
            require(
                swapThresholdPrice >= avgSqrtRatioX96 - maxSlippage,
                "high slippage"
            );
        } else {
            require(
                swapThresholdPrice <= avgSqrtRatioX96 + maxSlippage,
                "high slippage"