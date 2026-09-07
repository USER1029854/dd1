// Deployed ARB Automator impl 0x0338c2d1908549f4fcbca9da84039de1bac5c6c1 (Arbiscan-verified)
// The fund-authorizing flaw, verbatim from runtime-bound source:

function mintProducts(
        ProductMint[] calldata products,
        bytes calldata signature
    ) external nonReentrant {
        bytes32 signatures;
        for (uint256 i = 0; i < products.length; i++) {
            require(vaults[products[i].vault], "Automator: invalid vault");
            IVault(products[i].vault).mint(
                products[i].totalCollateral,
                products[i].mintParams,
                referral
            );
            uint256 collateralAtRiskPercentage = products[i].mintParams.collateralAtRisk * 1e18 / products[i].totalCollateral;
            bytes32 id = keccak256(abi.encodePacked(products[i].vault, products[i].mintParams.expiry, products[i].mintParams.anchorPrices, collateralAtRiskPercentage));
            _positions[id] = _positions[id] + products[i].totalCollateral - products[i].mintParams.makerCollateral;
            signatures = signatures ^ keccak256(abi.encodePacked(products[i].mintParams.maker, products[i].mintParams.makerSignature));
        }

        (address signer, ) = signatures.toEthSignedMessageHash().tryRecover(signature);
        require(makers[signer], "Automator: invalid maker");
        require(collateral.balanceOf(address(this)) >= totalFee + totalPendingRedemptions * getPricePerShare() / 1e18, "Automator: no enough collateral to redeem");

        emit ProductsMinted(products);
    }

    function burnProduct