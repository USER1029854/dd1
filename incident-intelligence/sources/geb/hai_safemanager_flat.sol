// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.20;

import {SAFEHandler} from '@contracts/proxies/SAFEHandler.sol';
import {ISAFEEngine} from '@interfaces/ISAFEEngine.sol';
import {ILiquidationEngine} from '@interfaces/ILiquidationEngine.sol';

import {Math} from '@libraries/Math.sol';
import {EnumerableSet} from '@openzeppelin/contracts/utils/structs/EnumerableSet.sol';
import {Assertions} from '@libraries/Assertions.sol';

import {IHaiSafeManager} from '@interfaces/proxies/IHaiSafeManager.sol';

/**
 * @title  HaiSafeManager
 * @notice This contract acts as interface to the SAFEEngine, facilitating the management of SAFEs
 * @dev    This contract is meant to be used by users that interact with the protocol through a proxy contract
 */
contract HaiSafeManager is IHaiSafeManager {
  using Math for uint256;
  using EnumerableSet for EnumerableSet.UintSet;
  using Assertions for address;

  // --- Registry ---

  /// @inheritdoc IHaiSafeManager
  address public safeEngine;

  // --- Data ---

  /// @notice Nonce used to generate safe ids (autoincremental)
  uint256 internal _safeId;
  /// @notice Mapping of user addresses to their enumerable set of safes
  mapping(address _safeOwner => EnumerableSet.UintSet) internal _usrSafes;
  /// @notice Mapping of user addresses to their enumerable set of safes per collateral type
  mapping(address _safeOwner => mapping(bytes32 _cType => EnumerableSet.UintSet)) internal _usrSafesPerCollat;
  /// @notice Mapping of safe ids to their data
  mapping(uint256 _safeId => SAFEData) internal _safeData;

  /// @inheritdoc IHaiSafeManager
  mapping(address _owner => mapping(uint256 _safeId => mapping(address _caller => bool _ok))) public safeCan;
  /// @inheritdoc IHaiSafeManager
  mapping(address _safeHandler => mapping(address _caller => bool _ok)) public handlerCan;

  // --- Modifiers ---

  /**
   * @notice Checks if the sender is the owner of the safe or the safe has permissions to call the function
   * @param  _safe Id of the safe to check if msg.sender has permissions for
   */
  modifier safeAllowed(uint256 _safe) {
    address _owner = _safeData[_safe].owner;
    if (msg.sender != _owner && !safeCan[_owner][_safe][msg.sender]) revert SafeNotAllowed();
    _;
  }

  /**
   * @notice Checks if the sender is the safe handler has permissions to call the function
   * @param  _handler Address of the handler to check if msg.sender has permissions for
   */
  modifier handlerAllowed(address _handler) {
    if (msg.sender != _handler && !handlerCan[_handler][msg.sender]) revert HandlerNotAllowed();
    _;
  }

  // --- Init ---

  /**
   * @param  _safeEngine Address of the SAFEEngine
   */
  constructor(address _safeEngine) {
    safeEngine = _safeEngine.assertNonNull();
  }

  // --- Getters ---

  /// @inheritdoc IHaiSafeManager
  function getSafes(address _usr) external view returns (uint256[] memory _safes) {
    _safes = _usrSafes[_usr].values();
  }

  /// @inheritdoc IHaiSafeManager
  function getSafes(address _usr, bytes32 _cType) external view returns (uint256[] memory _safes) {
    _safes = _usrSafesPerCollat[_usr][_cType].values();
  }

  /// @inheritdoc IHaiSafeManager
  function getSafesData(address _usr)
    external
    view
    returns (uint256[] memory _safes, address[] memory _safeHandlers, bytes32[] memory _cTypes)
  {
    _safes = _usrSafes[_usr].values();
    _safeHandlers = new address[](_safes.length);
    _cTypes = new bytes32[](_safes.length);
    for (uint256 _i; _i < _safes.length; _i++) {
      _safeHandlers[_i] = _safeData[_safes[_i]].safeHandler;
      _cTypes[_i] = _safeData[_safes[_i]].collateralType;
    }
  }

  /// @inheritdoc IHaiSafeManager
  function safeData(uint256 _safe) external view returns (SAFEData memory _sData) {
    _sData = _safeData[_safe];
  }

  // --- Methods ---

  /// @inheritdoc IHaiSafeManager
  function allowSAFE(uint256 _safe, address _usr, bool _ok) external safeAllowed(_safe) {
    address _owner = _safeData[_safe].owner;
    safeCan[_owner][_safe][_usr] = _ok;
    emit AllowSAFE(msg.sender, _safe, _usr, _ok);
  }

  /// @inheritdoc IHaiSafeManager
  function allowHandler(address _usr, bool _ok) external {
    handlerCan[msg.sender][_usr] = _ok;
    emit AllowHandler(msg.sender, _usr, _ok);
  }

  /// @inheritdoc IHaiSafeManager
  function openSAFE(bytes32 _cType, address _usr) external returns (uint256 _id) {
    if (_usr == address(0)) revert ZeroAddress();

    ++_safeId;
    address _safeHandler = address(new SAFEHandler(safeEngine));

    _safeData[_safeId] =
      SAFEData({owner: _usr, pendingOwner: address(0), safeHandler: _safeHandler, collateralType: _cType});

    _usrSafes[_usr].add(_safeId);
    _usrSafesPerCollat[_usr][_cType].add(_safeId);

    emit OpenSAFE(msg.sender, _usr, _safeId);
    return _safeId;
  }

  /// @inheritdoc IHaiSafeManager
  function transferSAFEOwnership(uint256 _safe, address _dst) external safeAllowed(_safe) {
    SAFEData memory _sData = _safeData[_safe];
    if (_dst == _sData.owner) revert AlreadySafeOwner();

    _safeData[_safe].pendingOwner = _dst;
    emit InitiateTransferSAFEOwnership(msg.sender, _safe, _dst);
  }

  /// @inheritdoc IHaiSafeManager
  function acceptSAFEOwnership(uint256 _safe) external {
    SAFEData memory _sData = _safeData[_safe];
    address _newOwner = _sData.pendingOwner;
    address _prevOwner = _sData.owner;

    if (msg.sender != _newOwner) revert SafeNotAllowed();

    _usrSafes[_prevOwner].remove(_safe);
    _usrSafesPerCollat[_prevOwner][_sData.collateralType].remove(_safe);

    _usrSafes[_newOwner].add(_safe);
    _usrSafesPerCollat[_newOwner][_sData.collateralType].add(_safe);

    _safeData[_safe].owner = _newOwner;
    _safeData[_safe].pendingOwner = address(0);

    emit TransferSAFEOwnership(_prevOwner, _safe, _newOwner);
  }

  /// @inheritdoc IHaiSafeManager
  function modifySAFECollateralization(
    uint256 _safe,
    int256 _deltaCollateral,
    int256 _deltaDebt
  ) external safeAllowed(_safe) {
    SAFEData memory _sData = _safeData[_safe];
    ISAFEEngine(safeEngine).modifySAFECollateralization(
      _sData.collateralType, _sData.safeHandler, _sData.safeHandler, _sData.safeHandler, _deltaCollateral, _deltaDebt
    );
    emit ModifySAFECollateralization(msg.sender, _safe, _deltaCollateral, _deltaDebt);
  }

  /// @inheritdoc IHaiSafeManager
  function transferCollateral(uint256 _safe, address _dst, uint256 _wad) external safeAllowed(_safe) {
    SAFEData memory _sData = _safeData[_safe];
    ISAFEEngine(safeEngine).transferCollateral(_sData.collateralType, _sData.safeHandler, _dst, _wad);
    emit TransferCollateral(msg.sender, _safe, _dst, _wad);
  }

  /// @inheritdoc IHaiSafeManager
  function transferCollateral(bytes32 _cType, uint256 _safe, address _dst, uint256 _wad) external safeAllowed(_safe) {
    SAFEData memory _sData = _safeData[_safe];
    ISAFEEngine(safeEngine).transferCollateral(_cType, _sData.safeHandler, _dst, _wad);
    emit TransferCollateral(msg.sender, _cType, _safe, _dst, _wad);
  }

  /// @inheritdoc IHaiSafeManager
  function transferInternalCoins(uint256 _safe, address _dst, uint256 _rad) external safeAllowed(_safe) {
    SAFEData memory _sData = _safeData[_safe];
    ISAFEEngine(safeEngine).transferInternalCoins(_sData.safeHandler, _dst, _rad);
    emit TransferInternalCoins(msg.sender, _safe, _dst, _rad);
  }

  /// @inheritdoc IHaiSafeManager
  function quitSystem(uint256 _safe, address _dst) external safeAllowed(_safe) handlerAllowed(_dst) {
    SAFEData memory _sData = _safeData[_safe];
    ISAFEEngine.SAFE memory _safeInfo = ISAFEEngine(safeEngine).safes(_sData.collateralType, _sData.safeHandler);
    int256 _deltaCollateral = _safeInfo.lockedCollateral.toInt();
    int256 _deltaDebt = _safeInfo.generatedDebt.toInt();
    ISAFEEngine(safeEngine).transferSAFECollateralAndDebt(
      _sData.collateralType, _sData.safeHandler, _dst, _deltaCollateral, _deltaDebt
    );

    // Remove safe from owner's list (notice it doesn't erase safe ownership)
    _usrSafes[_sData.owner].remove(_safe);
    _usrSafesPerCollat[_sData.owner][_sData.collateralType].remove(_safe);
    emit QuitSystem(msg.sender, _safe, _dst);
  }

  /// @inheritdoc IHaiSafeManager
  function enterSystem(address _src, uint256 _safe) external handlerAllowed(_src) safeAllowed(_safe) {
    SAFEData memory _sData = _safeData[_safe];
    ISAFEEngine.SAFE memory _safeInfo = ISAFEEngine(safeEngine).safes(_sData.collateralType, _sData.safeHandler);
    int256 _deltaCollateral = _safeInfo.lockedCollateral.toInt();
    int256 _deltaDebt = _safeInfo.generatedDebt.toInt();
    ISAFEEngine(safeEngine).transferSAFECollateralAndDebt(
      _sData.collateralType, _src, _sData.safeHandler, _deltaCollateral, _deltaDebt
    );
    emit EnterSystem(msg.sender, _src, _safe);
  }

  /// @inheritdoc IHaiSafeManager
  function moveSAFE(uint256 _safeSrc, uint256 _safeDst) external safeAllowed(_safeSrc) safeAllowed(_safeDst) {
    SAFEData memory _srcData = _safeData[_safeSrc];
    SAFEData memory _dstData = _safeData[_safeDst];
    if (_srcData.collateralType != _dstData.collateralType) revert CollateralTypesMismatch();
    ISAFEEngine.SAFE memory _safeInfo = ISAFEEngine(safeEngine).safes(_srcData.collateralType, _srcData.safeHandler);
    int256 _deltaCollateral = _safeInfo.lockedCollateral.toInt();
    int256 _deltaDebt = _safeInfo.generatedDebt.toInt();
    ISAFEEngine(safeEngine).transferSAFECollateralAndDebt(
      _srcData.collateralType, _srcData.safeHandler, _dstData.safeHandler, _deltaCollateral, _deltaDebt
    );

    // Remove safe from owner's list (notice it doesn't erase safe ownership)
    _usrSafes[_srcData.owner].remove(_safeSrc);
    _usrSafesPerCollat[_srcData.owner][_srcData.collateralType].remove(_safeSrc);
    emit MoveSAFE(msg.sender, _safeSrc, _safeDst);
  }

  /// @inheritdoc IHaiSafeManager
  function addSAFE(uint256 _safe) external {
    SAFEData memory _sData = _safeData[_safe];
    _usrSafes[msg.sender].add(_safe);
    _usrSafesPerCollat[msg.sender][_sData.collateralType].add(_safe);
  }

  /// @inheritdoc IHaiSafeManager
  function removeSAFE(uint256 _safe) external safeAllowed(_safe) {
    SAFEData memory _sData = _safeData[_safe];
    _usrSafes[_sData.owner].remove(_safe);
    _usrSafesPerCollat[_sData.owner][_sData.collateralType].remove(_safe);
  }

  /// @inheritdoc IHaiSafeManager
  function protectSAFE(uint256 _safe, address _liquidationEngine, address _saviour) external safeAllowed(_safe) {
    SAFEData memory _sData = _safeData[_safe];
    ILiquidationEngine(_liquidationEngine).protectSAFE(_sData.collateralType, _sData.safeHandler, _saviour);
    emit ProtectSAFE(msg.sender, _safe, _liquidationEngine, _saviour);
  }
}

// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.20;

import {ISAFEEngine} from '@interfaces/ISAFEEngine.sol';

/**
 * @title  SAFEHandler
 * @notice This contract is spawned to provide a unique safe handler address for each user's SAFE
 * @dev    When a new SAFE is created inside HaiSafeManager, this contract is deployed and calls the SAFEEngine to add permissions to the SAFE manager
 */
contract SAFEHandler {
  /**
   * @dev    Grants permissions to the SAFE manager to modify the SAFE of this contract's address
   * @param  _safeEngine Address of the SAFEEngine contract
   */
  constructor(address _safeEngine) {
    ISAFEEngine(_safeEngine).approveSAFEModification(msg.sender);
  }
}

// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.20;

import {IAuthorizable} from '@interfaces/utils/IAuthorizable.sol';
import {IModifiable} from '@interfaces/utils/IModifiable.sol';
import {IModifiablePerCollateral} from '@interfaces/utils/IModifiablePerCollateral.sol';
import {IDisableable} from '@interfaces/utils/IDisableable.sol';

interface ISAFEEngine is IAuthorizable, IDisableable, IModifiable, IModifiablePerCollateral {
  // --- Events ---

  /**
   * @notice Emitted when an address authorizes another address to modify its SAFE
   * @param _sender Address that sent the authorization
   * @param _account Address that is authorized to modify the SAFE
   */
  event ApproveSAFEModification(address _sender, address _account);

  /**
   * @notice Emitted when an address denies another address to modify its SAFE
   * @param _sender Address that sent the denial
   * @param _account Address that is denied to modify the SAFE
   */
  event DenySAFEModification(address _sender, address _account);

  /**
   * @notice Emitted when collateral is transferred between accounts
   * @param _cType Bytes32 representation of the collateral type
   * @param _src Address that sent the collateral
   * @param _dst Address that received the collateral
   * @param _wad Amount of collateral transferred
   */
  event TransferCollateral(bytes32 indexed _cType, address indexed _src, address indexed _dst, uint256 _wad);

  /**
   * @notice Emitted when internal coins are transferred between accounts
   * @param _src Address that sent the coins
   * @param _dst Address that received the coins
   * @param _rad Amount of coins transferred
   */
  event TransferInternalCoins(address indexed _src, address indexed _dst, uint256 _rad);

  /**
   * @notice Emitted when the SAFE state is modified by the owner or authorized accounts
   * @param _cType Bytes32 representation of the collateral type
   * @param _safe Address of the SAFE
   * @param _collateralSource Address that sent/receives the collateral
   * @param _debtDestination Address that sent/receives the debt
   * @param _deltaCollateral Amount of collateral added/extracted from the SAFE [wad]
   * @param _deltaDebt Amount of debt to generate/repay [wad]
   */
  event ModifySAFECollateralization(
    bytes32 indexed _cType,
    address indexed _safe,
    address _collateralSource,
    address _debtDestination,
    int256 _deltaCollateral,
    int256 _deltaDebt
  );

  /**
   * @notice Emitted when collateral and/or debt is transferred between SAFEs
   * @param _cType Bytes32 representation of the collateral type
   * @param _src Address that sent the collateral
   * @param _dst Address that received the collateral
   * @param _deltaCollateral Amount of collateral to take/add into src and give/take from dst [wad]
   * @param _deltaDebt Amount of debt to take/add into src and give/take from dst [wad]
   */
  event TransferSAFECollateralAndDebt(
    bytes32 indexed _cType, address indexed _src, address indexed _dst, int256 _deltaCollateral, int256 _deltaDebt
  );

  /**
   * @notice Emitted when collateral and debt is confiscated from a SAFE
   * @param _cType Bytes32 representation of the collateral type
   * @param _safe Address of the SAFE
   * @param _collateralSource Address that sent/receives the collateral
   * @param _debtDestination Address that sent/receives the debt
   * @param _deltaCollateral Amount of collateral added/extracted from the SAFE [wad]
   * @param _deltaDebt Amount of debt to generate/repay [wad]
   */
  event ConfiscateSAFECollateralAndDebt(
    bytes32 indexed _cType,
    address indexed _safe,
    address _collateralSource,
    address _debtDestination,
    int256 _deltaCollateral,
    int256 _deltaDebt
  );

  /**
   * @notice Emitted when an account's debt is settled with coins
   * @dev    Accounts (not SAFEs) can only settle unbacked debt
   * @param _account Address of the account
   * @param _rad Amount of debt & coins to destroy
   */
  event SettleDebt(address indexed _account, uint256 _rad);

  /**
   * @notice Emitted when an unbacked debt is created to an account
   * @param _debtDestination Address that received the newly created debt
   * @param _coinDestination Address that received the newly created coins
   * @param _rad Amount of debt to create
   */
  event CreateUnbackedDebt(address indexed _debtDestination, address indexed _coinDestination, uint256 _rad);

  /**
   * @notice Emit when the accumulated rate of a collateral type is updated
   * @param _cType Bytes32 representation of the collateral type
   * @param _surplusDst Address that received the newly created surplus
   * @param _rateMultiplier Delta of the accumulated rate [ray]
   */
  event UpdateAccumulatedRate(bytes32 indexed _cType, address _surplusDst, int256 _rateMultiplier);

  /**
   * @notice Emitted when the safety price and liquidation price of a collateral type is updated
   * @param _cType Bytes32 representation of the collateral type
   * @param _safetyPrice New price at which a SAFE is allowed to generate debt [ray]
   * @param _liquidationPrice New price at which a SAFE gets liquidated [ray]
   */
  event UpdateCollateralPrice(bytes32 indexed _cType, uint256 _safetyPrice, uint256 _liquidationPrice);

  // --- Errors ---

  /// @notice Throws when trying to modify parameters of an uninitialized collateral type
  error SAFEEng_CollateralTypeNotInitialized();
  /// @notice Throws when trying to modify a SAFE into an unsafe state
  error SAFEEng_SAFENotSafe();
  /// @notice Throws when trying to modify a SAFE into a dusty safe (debt non-zero and below `debtFloor`)
  error SAFEEng_DustySAFE();
  /// @notice Throws when trying to generate debt that would put the system over the global debt ceiling
  error SAFEEng_GlobalDebtCeilingHit();
  /// @notice Throws when trying to generate debt that would put the system over the collateral debt ceiling
  error SAFEEng_CollateralDebtCeilingHit();
  /// @notice Throws when trying to generate debt that would put the SAFE over the SAFE debt ceiling
  error SAFEEng_SAFEDebtCeilingHit();
  /// @notice Throws when an account tries to modify a SAFE without the proper permissions
  error SAFEEng_NotSAFEAllowed();
  /// @notice Throws when an account tries to pull collateral from a SAFE without the proper permissions
  error SAFEEng_NotCollateralSrcAllowed();
  /// @notice Throws when an account tries to push debt to a SAFE without the proper permissions
  error SAFEEng_NotDebtDstAllowed();

  // --- Structs ---

  struct SAFE {
    // Total amount of collateral locked in a SAFE
    uint256 /* WAD */ lockedCollateral;
    // Total amount of debt generated by a SAFE
    uint256 /* WAD */ generatedDebt;
  }

  struct SAFEEngineParams {
    // Total amount of debt that a single safe can generate
    uint256 /* WAD */ safeDebtCeiling;
    // Maximum amount of debt that can be issued across all safes
    uint256 /* RAD */ globalDebtCeiling;
  }

  struct SAFEEngineCollateralData {
    // Total amount of debt issued by the collateral type
    uint256 /* WAD */ debtAmount;
    // Total amount of collateral locked in SAFEs using the collateral type
    uint256 /* WAD */ lockedAmount;
    // Accumulated rate of the collateral type
    uint256 /* RAY */ accumulatedRate;
    // Floor price at which a SAFE is allowed to generate debt
    uint256 /* RAY */ safetyPrice;
    // Price at which a SAFE gets liquidated
    uint256 /* RAY */ liquidationPrice;
  }

  struct SAFEEngineCollateralParams {
    // Maximum amount of debt that can be generated with the collateral type
    uint256 /* RAD */ debtCeiling;
    // Minimum amount of debt that must be generated by a SAFE using the collateral
    uint256 /* RAD */ debtFloor;
  }

  // --- Data ---

  /**
   * @notice Getter for the contract parameters struct
   * @return _safeEngineParams The active SAFEEngineParams
   */
  function params() external view returns (SAFEEngineParams memory _safeEngineParams);

  /**
   * @notice Getter for the unpacked contract parameters struct
   * @return _safeDebtCeiling Total amount of debt that a single safe can generate [wad]
   * @return _globalDebtCeiling Maximum amount of debt that can be issued [rad]
   */
  // solhint-disable-next-line private-vars-leading-underscore
  function _params() external view returns (uint256 _safeDebtCeiling, uint256 _globalDebtCeiling);

  /**
   * @notice Getter for the collateral parameters struct
   * @param  _cType Bytes32 representation of the collateral type
   * @return  _safeEngineCParams SAFEEngineCollateralParams for the collateral type
   */
  function cParams(bytes32 _cType) external view returns (SAFEEngineCollateralParams memory _safeEngineCParams);

  /**
   * @notice Getter for the unpacked collateral parameters struct
   * @param  _cType Bytes32 representation of the collateral type
   * @return _debtCeiling Maximum amount of debt that can be generated with this collateral type
   * @return _debtFloor Minimum amount of debt that must be generated by a SAFE using this collateral
   */
  // solhint-disable-next-line private-vars-leading-underscore
  function _cParams(bytes32 _cType) external view returns (uint256 _debtCeiling, uint256 _debtFloor);

  /**
   * @notice Getter for the collateral data struct
   * @param  _cType Bytes32 representation of the collateral type
   * @return  _safeEngineCData SAFEEngineCollateralData for the collateral type
   */
  function cData(bytes32 _cType) external view returns (SAFEEngineCollateralData memory _safeEngineCData);

  /**
   * @notice Getter for the unpacked collateral data struct
   * @param  _cType Bytes32 representation of the collateral type
   * @return _debtAmount Total amount of debt issued by a collateral type [wad]
   * @return _lockedAmount Total amount of collateral locked in all SAFEs of the collateral type [wad]
   * @return _accumulatedRate Accumulated rate of a collateral type [ray]
   * @return _safetyPrice Floor price at which a SAFE is allowed to generate debt [ray]
   * @return _liquidationPrice Price at which a SAFE gets liquidated [ray]
   */
  // solhint-disable-next-line private-vars-leading-underscore
  function _cData(bytes32 _cType)
    external
    view
    returns (
      uint256 _debtAmount,
      uint256 _lockedAmount,
      uint256 _accumulatedRate,
      uint256 _safetyPrice,
      uint256 _liquidationPrice
    );

  /**
   * @notice Data about each SAFE
   * @param  _cType Bytes32 representation of the collateral type
   * @param  _safeAddress Address of the SAFE
   * @return _safeData SAFE data for the specified collateral type of the specified safe.
   */
  function safes(bytes32 _cType, address _safeAddress) external view returns (SAFE memory _safeData);

  /**
   * @notice Unpacked data about each SAFE
   * @param  _cType Bytes32 representation of the collateral type
   * @param  _safeAddress Address of the SAFE
   * @return _lockedCollateral Total amount of collateral locked in a SAFE [wad]
   * @return _generatedDebt Total amount of debt generated by a SAFE [wad]
   */
  // solhint-disable-next-line private-vars-leading-underscore
  function _safes(
    bytes32 _cType,
    address _safeAddress
  ) external view returns (uint256 _lockedCollateral, uint256 _generatedDebt);

  /**
   * @notice Who can transfer collateral & debt in/out of a SAFE
   * @param  _caller Address to check for SAFE permissions for
   * @param  _account Account to check if caller has permissions for
   * @return _safeRights Boolean representation of the SAFE rights (0/1)
   */
  function safeRights(address _caller, address _account) external view returns (bool _safeRights);

  // --- Balances ---

  /**
   * @notice Balance of each collateral type
   * @param  _cType Bytes32 representation of the collateral type to check balance for
   * @param  _account Account to check balance for
   * @return _collateralBalance Collateral balance of the account [wad]
   */
  function tokenCollateral(bytes32 _cType, address _account) external view returns (uint256 _collateralBalance);

  /**
   * @notice Internal balance of system coins held by an account
   * @param  _account Account to check balance for
   * @return _balance Internal coin balance of the account [rad]
   */
  function coinBalance(address _account) external view returns (uint256 _balance);

  /**
   * @notice Amount of debt held by an account
   * @param  _account Account to check balance for
   * @return _debtBalance Debt balance of the account [rad]
   */
  function debtBalance(address _account) external view returns (uint256 _debtBalance);

  /**
   * @notice Total amount of debt (coins) currently issued
   * @return _globalDebt Global debt [rad]
   */
  function globalDebt() external returns (uint256 _globalDebt);

  /**
   * @notice 'Bad' debt that's not covered by collateral
   * @return _globalUnbackedDebt Global unbacked debt [rad]
   */
  function globalUnbackedDebt() external view returns (uint256 _globalUnbackedDebt);

  // --- Init ---

  // --- Fungibility ---

  /**
   * @notice Transfer collateral between accounts
   * @param _cType Collateral type transferred
   * @param _source Collateral source
   * @param _destination Collateral destination
   * @param _wad Amount of collateral transferred
   */
  function transferCollateral(bytes32 _cType, address _source, address _destination, uint256 _wad) external;

  /**
   * @notice Transfer internal coins (does not affect external balances from Coin.sol)
   * @param  _source Coins source
   * @param  _destination Coins destination
   * @param  _rad Amount of coins transferred
   */
  function transferInternalCoins(address _source, address _destination, uint256 _rad) external;

  /**
   * @notice Join/exit collateral into and and out of the system
   * @param _cType Collateral type to join/exit
   * @param _account Account that gets credited/debited
   * @param _wad Amount of collateral
   */
  function modifyCollateralBalance(bytes32 _cType, address _account, int256 _wad) external;

  // --- SAFE Manipulation ---

  /**
   * @notice Add/remove collateral or put back/generate more debt in a SAFE
   * @param _cType Type of collateral to withdraw/deposit in and from the SAFE
   * @param _safe Target SAFE
   * @param _collateralSource Account we take collateral from/put collateral into
   * @param _debtDestination Account from which we credit/debit coins and debt
   * @param _deltaCollateral Amount of collateral added/extracted from the SAFE [wad]
   * @param _deltaDebt Amount of debt to generate/repay [wad]
   */
  function modifySAFECollateralization(
    bytes32 _cType,
    address _safe,
    address _collateralSource,
    address _debtDestination,
    int256 /* WAD */ _deltaCollateral,
    int256 /* WAD */ _deltaDebt
  ) external;

  // --- SAFE Fungibility ---

  /**
   * @notice Transfer collateral and/or debt between SAFEs
   * @param _cType Collateral type transferred between SAFEs
   * @param _src Source SAFE
   * @param _dst Destination SAFE
   * @param _deltaCollateral Amount of collateral to take/add into src and give/take from dst [wad]
   * @param _deltaDebt Amount of debt to take/add into src and give/take from dst [wad]
   */
  function transferSAFECollateralAndDebt(
    bytes32 _cType,
    address _src,
    address _dst,
    int256 /* WAD */ _deltaCollateral,
    int256 /* WAD */ _deltaDebt
  ) external;

  // --- SAFE Confiscation ---

  /**
   * @notice Normally used by the LiquidationEngine in order to confiscate collateral and
   *      debt from a SAFE and give them to someone else
   * @param _cType Collateral type the SAFE has locked inside
   * @param _safe Target SAFE
   * @param _collateralSource Who we take/give collateral to
   * @param _debtDestination Who we take/give debt to
   * @param _deltaCollateral Amount of collateral taken/added into the SAFE [wad]
   * @param _deltaDebt Amount of debt taken/added into the SAFE [wad]
   */
  function confiscateSAFECollateralAndDebt(
    bytes32 _cType,
    address _safe,
    address _collateralSource,
    address _debtDestination,
    int256 _deltaCollateral,
    int256 _deltaDebt
  ) external;

  // --- Settlement ---

  /**
   * @notice Nullify an amount of coins with an equal amount of debt
   * @dev    Coins & debt are like matter and antimatter, they nullify each other
   * @param  _rad Amount of debt & coins to destroy
   */
  function settleDebt(uint256 _rad) external;

  /**
   * @notice Allows an authorized contract to create debt without collateral
   * @param _debtDestination The account that will receive the newly created debt
   * @param _coinDestination The account that will receive the newly created coins
   * @param _rad Amount of debt to create
   * @dev   Usually called by DebtAuctionHouse in order to terminate auctions prematurely post settlement
   */
  function createUnbackedDebt(address _debtDestination, address _coinDestination, uint256 _rad) external;

  // --- Update ---

  /**
   * @notice Allows an authorized contract to accrue interest on a specific collateral type
   * @param _cType Collateral type we accrue interest for
   * @param _surplusDst Destination for the newly created surplus
   * @param _rateMultiplier Multiplier applied to the debtAmount in order to calculate the surplus [ray]
   * @dev   The rateMultiplier is usually calculated by the TaxCollector contract
   */
  function updateAccumulatedRate(bytes32 _cType, address _surplusDst, int256 _rateMultiplier) external;

  /**
   * @notice Allows an authorized contract to update the safety price and liquidation price of a collateral type
   * @param _cType Collateral type we update the prices for
   * @param _safetyPrice New safety price [ray]
   * @param _liquidationPrice New liquidation price [ray]
   */
  function updateCollateralPrice(bytes32 _cType, uint256 _safetyPrice, uint256 _liquidationPrice) external;

  // --- Authorization ---

  /**
   * @notice Allow an address to modify your SAFE
   * @param _account Account to give SAFE permissions to
   */
  function approveSAFEModification(address _account) external;

  /**
   * @notice Deny an address the rights to modify your SAFE
   * @param _account Account that is denied SAFE permissions
   */
  function denySAFEModification(address _account) external;

  /**
   * @notice Checks whether an account has the right to modify a SAFE
   * @param _safe The safe to check
   * @param _account The account to check
   * @return _allowed Whether the account can modify the safe
   */
  function canModifySAFE(address _safe, address _account) external view returns (bool _allowed);
}

// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.20;

import {ISAFEEngine} from '@interfaces/ISAFEEngine.sol';
import {IAccountingEngine} from '@interfaces/IAccountingEngine.sol';

import {IAuthorizable} from '@interfaces/utils/IAuthorizable.sol';
import {IModifiable} from '@interfaces/utils/IModifiable.sol';
import {IModifiablePerCollateral} from '@interfaces/utils/IModifiablePerCollateral.sol';
import {IDisableable} from '@interfaces/utils/IDisableable.sol';

interface ILiquidationEngine is IAuthorizable, IDisableable, IModifiable, IModifiablePerCollateral {
  // --- Events ---

  /**
   * @notice Emitted when a SAFE saviour contract is added to the allowlist
   * @param  _saviour SAFE saviour contract being allowlisted
   */
  event ConnectSAFESaviour(address _saviour);

  /**
   * @notice Emitted when a SAFE saviour contract is removed from the allowlist
   * @param  _saviour SAFE saviour contract being removed from the allowlist
   */
  event DisconnectSAFESaviour(address _saviour);

  /**
   * @notice Emitted when the current on auction system coins counter is updated
   * @param  _currentOnAuctionSystemCoins New value of the current on auction system coins counter
   */
  event UpdateCurrentOnAuctionSystemCoins(uint256 _currentOnAuctionSystemCoins);

  /**
   * @notice Emitted when a SAFE is liquidated
   * @param  _cType Bytes32 representation of the collateral type
   * @param  _safe Address of the SAFE being liquidated
   * @param  _collateralAmount Amount of collateral being confiscated [wad]
   * @param  _debtAmount Amount of debt being transferred [wad]
   * @param  _amountToRaise Amount of system coins to raise in the collateral auction [rad]
   * @param  _collateralAuctioneer Address of the collateral auctioneer contract handling the collateral auction
   * @param  _auctionId Id of the collateral auction
   */
  event Liquidate(
    bytes32 indexed _cType,
    address indexed _safe,
    uint256 _collateralAmount,
    uint256 _debtAmount,
    uint256 _amountToRaise,
    address _collateralAuctioneer,
    uint256 _auctionId
  );

  /**
   * @notice Emitted when a SAFE is saved from being liquidated by a SAFE saviour contract
   * @param  _cType Bytes32 representation of the collateral type
   * @param  _safe Address of the SAFE being saved
   * @param  _collateralAddedOrDebtRepaid Amount of collateral being added or debt repaid [wad]
   */
  event SaveSAFE(bytes32 indexed _cType, address indexed _safe, uint256 _collateralAddedOrDebtRepaid);

  /**
   * @notice Emitted when a SAFE saviour action is unsuccessful
   * @param  _failReason Reason why the SAFE saviour action failed
   */
  event FailedSAFESave(bytes _failReason);

  /**
   * @notice Emitted when a SAFE saviour contract is chosen for a SAFE
   * @param  _cType Bytes32 representation of the collateral type
   * @param  _safe Address of the SAFE being saved
   * @param  _saviour Address of the SAFE saviour contract chosen
   */
  event ProtectSAFE(bytes32 indexed _cType, address indexed _safe, address _saviour);

  // --- Errors ---

  /// @notice Throws when trying to add a reverting SAFE saviour to the allowlist
  error LiqEng_SaviourNotOk();
  /// @notice Throws when trying to add an invalid SAFE saviour to the allowlist
  error LiqEng_InvalidAmounts();
  /// @notice Throws when trying to choose a SAFE saviour for a SAFE without the proper authorization
  error LiqEng_CannotModifySAFE();
  /// @notice Throws when trying to choose a SAFE saviour that is not on the allowlist
  error LiqEng_SaviourNotAuthorized();
  /// @notice Throws when trying to liquidate a SAFE that is not unsafe
  error LiqEng_SAFENotUnsafe();
  /// @notice Throws when trying to simultaneously liquidate more debt than the limit allows
  error LiqEng_LiquidationLimitHit();
  /// @notice Throws when SAFE saviour action is invalid during a liquidation
  error LiqEng_InvalidSAFESaviourOperation();
  /// @notice Throws when trying to liquidate a SAFE with a null amount of debt
  error LiqEng_NullAuction();
  /// @notice Throws when trying to liquidate a SAFE with a null amount of collateral to sell
  error LiqEng_NullCollateralToSell();
  /// @notice Throws when trying to call a function only the liquidator is allowed to call
  error LiqEng_OnlyLiqEng();

  // --- Structs ---

  struct LiquidationEngineParams {
    // Max amount of system coins to be auctioned at the same time
    uint256 /* RAD */ onAuctionSystemCoinLimit;
    // The gas limit for the saviour call
    uint256 /*       */ saviourGasLimit;
  }

  struct LiquidationEngineCollateralParams {
    // Address of the collateral auction house handling liquidations for this collateral type
    address /*       */ collateralAuctionHouse;
    // Penalty applied to every liquidation involving this collateral type
    uint256 /* WAD % */ liquidationPenalty;
    // Max amount of system coins to request in one auction for this collateral type
    uint256 /* RAD   */ liquidationQuantity;
  }

  // --- Registry ---

  /**
   * @notice The SAFEEngine is used to query the state of the SAFEs, confiscate the collateral and transfer the debt
   * @return _safeEngine Address of the contract that handles the state of the SAFEs
   */
  function safeEngine() external view returns (ISAFEEngine _safeEngine);

  /**
   * @notice The AccountingEngine is used to push the debt into the system, and set as the first bidder on the collateral auctions
   * @return _accountingEngine Address of the AccountingEngine
   */
  function accountingEngine() external view returns (IAccountingEngine _accountingEngine);

  // --- Params ---

  /**
   * @notice Getter for the contract parameters struct
   * @return _liqEngineParams LiquidationEngine parameters struct
   */
  function params() external view returns (LiquidationEngineParams memory _liqEngineParams);

  /**
   * @notice Getter for the unpacked contract parameters struct
   * @return _onAuctionSystemCoinLimit Max amount of system coins to be auctioned at the same time [rad]
   */
  // solhint-disable-next-line private-vars-leading-underscore
  function _params() external view returns (uint256 _onAuctionSystemCoinLimit, uint256 _saviourGasLimit);

  /**
   * @notice Getter for the collateral parameters struct
   * @param  _cType Bytes32 representation of the collateral type
   * @return _liqEngineCParams LiquidationEngine collateral parameters struct
   */
  function cParams(bytes32 _cType) external view returns (LiquidationEngineCollateralParams memory _liqEngineCParams);

  /**
   * @notice Getter for the unpacked collateral parameters struct
   * @param  _cType Bytes32 representation of the collateral type
   * @return _collateralAuctionHouse Address of the collateral auction house handling liquidations
   * @return _liquidationPenalty Penalty applied to every liquidation involving this collateral type [wad%]
   * @return _liquidationQuantity Max amount of system coins to request in one auction for this collateral type [rad]
   */
  // solhint-disable-next-line private-vars-leading-underscore
  function _cParams(bytes32 _cType)
    external
    view
    returns (address _collateralAuctionHouse, uint256 _liquidationPenalty, uint256 _liquidationQuantity);

  // --- Data ---

  /**
   * @notice The limit adjusted debt to cover
   * @param  _cType The SAFE's collateral type
   * @param  _safe The SAFE's address
   * @return _wad The limit adjusted debt to cover
   */
  function getLimitAdjustedDebtToCover(bytes32 _cType, address _safe) external view returns (uint256 _wad);

  /// @notice Total amount of system coins currently being auctioned
  function currentOnAuctionSystemCoins() external view returns (uint256 _currentOnAuctionSystemCoins);

  // --- SAFE Saviours ---

  /**
   * @notice Allowed contracts that can be chosen to save SAFEs from liquidation
   * @param  _saviour The SAFE saviour contract to check
   * @return _canSave Whether the contract can save SAFEs or not
   */
  function safeSaviours(address _saviour) external view returns (bool _canSave);

  /**
   * @notice Saviour contract chosen for each SAFE by its owner
   * @param  _cType The SAFE's collateral type
   * @param  _safe The SAFE's address
   * @return _saviour The SAFE's saviour contract (address(0) if none)
   */
  function chosenSAFESaviour(bytes32 _cType, address _safe) external view returns (address _saviour);

  // --- Methods ---

  /**
   * @notice Remove debt that was being auctioned
   * @dev    Usually called by CollateralAuctionHouse when an auction is settled
   * @param  _rad The amount of debt in RAD to withdraw from `currentOnAuctionSystemCoins`
   */
  function removeCoinsFromAuction(uint256 _rad) external;

  /**
   * @notice Liquidate a SAFE
   * @dev    A SAFE can be liquidated if the accumulated debt plus the liquidation penalty is higher than the collateral value
   * @param  _cType The SAFE's collateral type
   * @param  _safe The SAFE's address
   * @return _auctionId The auction id of the collateral auction
   */
  function liquidateSAFE(bytes32 _cType, address _safe) external returns (uint256 _auctionId);

  /**
   * @notice Choose a saviour contract for your SAFE
   * @param  _cType The SAFE's collateral type
   * @param  _safe The SAFE's address
   * @param  _saviour The chosen saviour
   */
  function protectSAFE(bytes32 _cType, address _safe, address _saviour) external;

  // --- Administration ---

  /**
   * @notice Authed function to add contracts that can save SAFEs from liquidation
   * @param  _saviour SAFE saviour contract to be whitelisted
   */
  function connectSAFESaviour(address _saviour) external;

  /**
   * @notice Authed function to remove contracts that can save SAFEs from liquidation
   * @param  _saviour SAFE saviour contract to be removed
   */
  function disconnectSAFESaviour(address _saviour) external;
}

// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.20;

/// @dev Max uint256 value that a RAD can represent without overflowing
uint256 constant MAX_RAD = type(uint256).max / RAY;
/// @dev Uint256 representation of 1 RAD
uint256 constant RAD = 10 ** 45;
/// @dev Uint256 representation of 1 RAY
uint256 constant RAY = 10 ** 27;
/// @dev Uint256 representation of 1 WAD
uint256 constant WAD = 10 ** 18;
/// @dev Uint256 representation of 1 year in seconds
uint256 constant YEAR = 365 days;
/// @dev Uint256 representation of 1 hour in seconds
uint256 constant HOUR = 3600;

/**
 * @title Math
 * @notice This library contains common math functions
 */
library Math {
  // --- Errors ---

  /// @dev Throws when trying to cast a uint256 to an int256 that overflows
  error IntOverflow();

  // --- Math ---

  /**
   * @notice Calculates the sum of an unsigned integer and a signed integer
   * @param  _x Unsigned integer
   * @param  _y Signed integer
   * @return _add Unsigned sum of `_x` and `_y`
   */
  function add(uint256 _x, int256 _y) internal pure returns (uint256 _add) {
    if (_y >= 0) {
      return _x + uint256(_y);
    } else {
      return _x - uint256(-_y);
    }
  }

  /**
   * @notice Calculates the substraction of an unsigned integer and a signed integer
   * @param  _x Unsigned integer
   * @param  _y Signed integer
   * @return _sub Unsigned substraction of `_x` and `_y`
   */
  function sub(uint256 _x, int256 _y) internal pure returns (uint256 _sub) {
    if (_y >= 0) {
      return _x - uint256(_y);
    } else {
      return _x + uint256(-_y);
    }
  }

  /**
   * @notice Calculates the substraction of two unsigned integers
   * @param  _x Unsigned integer
   * @param  _y Unsigned integer
   * @return _sub Signed substraction of `_x` and `_y`
   */
  function sub(uint256 _x, uint256 _y) internal pure returns (int256 _sub) {
    return toInt(_x) - toInt(_y);
  }

  /**
   * @notice Calculates the multiplication of an unsigned integer and a signed integer
   * @param  _x Unsigned integer
   * @param  _y Signed integer
   * @return _mul Signed multiplication of `_x` and `_y`
   */
  function mul(uint256 _x, int256 _y) internal pure returns (int256 _mul) {
    return toInt(_x) * _y;
  }

  /**
   * @notice Calculates the multiplication of two unsigned RAY integers
   * @param  _x Unsigned RAY integer
   * @param  _y Unsigned RAY integer
   * @return _rmul Unsigned multiplication of `_x` and `_y` in RAY precision
   */
  function rmul(uint256 _x, uint256 _y) internal pure returns (uint256 _rmul) {
    return (_x * _y) / RAY;
  }

  /**
   * @notice Calculates the multiplication of an unsigned and a signed RAY integers
   * @param  _x Unsigned RAY integer
   * @param  _y Signed RAY integer
   * @return _rmul Signed multiplication of `_x` and `_y` in RAY precision
   */
  function rmul(uint256 _x, int256 _y) internal pure returns (int256 _rmul) {
    return (toInt(_x) * _y) / int256(RAY);
  }

  /**
   * @notice Calculates the multiplication of two unsigned WAD integers
   * @param  _x Unsigned WAD integer
   * @param  _y Unsigned WAD integer
   * @return _wmul Unsigned multiplication of `_x` and `_y` in WAD precision
   */
  function wmul(uint256 _x, uint256 _y) internal pure returns (uint256 _wmul) {
    return (_x * _y) / WAD;
  }

  /**
   * @notice Calculates the multiplication of an unsigned and a signed WAD integers
   * @param  _x Unsigned WAD integer
   * @param  _y Signed WAD integer
   * @return _wmul Signed multiplication of `_x` and `_y` in WAD precision
   */
  function wmul(uint256 _x, int256 _y) internal pure returns (int256 _wmul) {
    return (toInt(_x) * _y) / int256(WAD);
  }

  /**
   * @notice Calculates the multiplication of two signed WAD integers
   * @param  _x Signed WAD integer
   * @param  _y Signed WAD integer
   * @return _wmul Signed multiplication of `_x` and `_y` in WAD precision
   */
  function wmul(int256 _x, int256 _y) internal pure returns (int256 _wmul) {
    return (_x * _y) / int256(WAD);
  }

  /**
   * @notice Calculates the division of two unsigned RAY integers
   * @param  _x Unsigned RAY integer
   * @param  _y Unsigned RAY integer
   * @return _rdiv Unsigned division of `_x` by `_y` in RAY precision
   */
  function rdiv(uint256 _x, uint256 _y) internal pure returns (uint256 _rdiv) {
    return (_x * RAY) / _y;
  }

  /**
   * @notice Calculates the division of two signed RAY integers
   * @param  _x Signed RAY integer
   * @param  _y Signed RAY integer
   * @return _rdiv Signed division of `_x` by `_y` in RAY precision
   */
  function rdiv(int256 _x, int256 _y) internal pure returns (int256 _rdiv) {
    return (_x * int256(RAY)) / _y;
  }

  /**
   * @notice Calculates the division of two unsigned WAD integers
   * @param  _x Unsigned WAD integer
   * @param  _y Unsigned WAD integer
   * @return _wdiv Unsigned division of `_x` by `_y` in WAD precision
   */
  function wdiv(uint256 _x, uint256 _y) internal pure returns (uint256 _wdiv) {
    return (_x * WAD) / _y;
  }

  /**
   * @notice Calculates the power of an unsigned RAY integer to an unsigned integer
   * @param  _x Unsigned RAY integer
   * @param  _n Unsigned integer exponent
   * @return _rpow Unsigned `_x` to the power of `_n` in RAY precision
   */
  function rpow(uint256 _x, uint256 _n) internal pure returns (uint256 _rpow) {
    assembly {
      switch _x
      case 0 {
        switch _n
        case 0 { _rpow := RAY }
        default { _rpow := 0 }
      }
      default {
        switch mod(_n, 2)
        case 0 { _rpow := RAY }
        default { _rpow := _x }
        let half := div(RAY, 2) // for rounding.
        for { _n := div(_n, 2) } _n { _n := div(_n, 2) } {
          let _xx := mul(_x, _x)
          if iszero(eq(div(_xx, _x), _x)) { revert(0, 0) }
          let _xxRound := add(_xx, half)
          if lt(_xxRound, _xx) { revert(0, 0) }
          _x := div(_xxRound, RAY)
          if mod(_n, 2) {
            let _zx := mul(_rpow, _x)
            if and(iszero(iszero(_x)), iszero(eq(div(_zx, _x), _rpow))) { revert(0, 0) }
            let _zxRound := add(_zx, half)
            if lt(_zxRound, _zx) { revert(0, 0) }
            _rpow := div(_zxRound, RAY)
          }
        }
      }
    }
  }

  /**
   * @notice Calculates the maximum of two unsigned integers
   * @param  _x Unsigned integer
   * @param  _y Unsigned integer
   * @return _max Unsigned maximum of `_x` and `_y`
   */
  function max(uint256 _x, uint256 _y) internal pure returns (uint256 _max) {
    _max = (_x >= _y) ? _x : _y;
  }

  /**
   * @notice Calculates the minimum of two unsigned integers
   * @param  _x Unsigned integer
   * @param  _y Unsigned integer
   * @return _min Unsigned minimum of `_x` and `_y`
   */
  function min(uint256 _x, uint256 _y) internal pure returns (uint256 _min) {
    _min = (_x <= _y) ? _x : _y;
  }

  /**
   * @notice Casts an unsigned integer to a signed integer
   * @param  _x Unsigned integer
   * @return _int Signed integer
   * @dev    Throws if `_x` is too large to fit in an int256
   */
  function toInt(uint256 _x) internal pure returns (int256 _int) {
    _int = int256(_x);
    if (_int < 0) revert IntOverflow();
  }

  // --- PI Specific Math ---

  /**
   * @notice Calculates the Riemann sum of two signed integers
   * @param  _x Signed integer
   * @param  _y Signed integer
   * @return _riemannSum Riemann sum of `_x` and `_y`
   */
  function riemannSum(int256 _x, int256 _y) internal pure returns (int256 _riemannSum) {
    return (_x + _y) / 2;
  }

  /**
   * @notice Calculates the absolute value of a signed integer
   * @param  _x Signed integer
   * @return _z Unsigned absolute value of `_x`
   */
  function absolute(int256 _x) internal pure returns (uint256 _z) {
    _z = (_x < 0) ? uint256(-_x) : uint256(_x);
  }
}

// SPDX-License-Identifier: MIT
// OpenZeppelin Contracts (last updated v5.0.0) (utils/structs/EnumerableSet.sol)
// This file was procedurally generated from scripts/generate/templates/EnumerableSet.js.

pragma solidity ^0.8.20;

/**
 * @dev Library for managing
 * https://en.wikipedia.org/wiki/Set_(abstract_data_type)[sets] of primitive
 * types.
 *
 * Sets have the following properties:
 *
 * - Elements are added, removed, and checked for existence in constant time
 * (O(1)).
 * - Elements are enumerated in O(n). No guarantees are made on the ordering.
 *
 * ```solidity
 * contract Example {
 *     // Add the library methods
 *     using EnumerableSet for EnumerableSet.AddressSet;
 *
 *     // Declare a set state variable
 *     EnumerableSet.AddressSet private mySet;
 * }
 * ```
 *
 * As of v3.3.0, sets of type `bytes32` (`Bytes32Set`), `address` (`AddressSet`)
 * and `uint256` (`UintSet`) are supported.
 *
 * [WARNING]
 * ====
 * Trying to delete such a structure from storage will likely result in data corruption, rendering the structure
 * unusable.
 * See https://github.com/ethereum/solidity/pull/11843[ethereum/solidity#11843] for more info.
 *
 * In order to clean an EnumerableSet, you can either remove all elements one by one or create a fresh instance using an
 * array of EnumerableSet.
 * ====
 */
library EnumerableSet {
    // To implement this library for multiple types with as little code
    // repetition as possible, we write it in terms of a generic Set type with
    // bytes32 values.
    // The Set implementation uses private functions, and user-facing
    // implementations (such as AddressSet) are just wrappers around the
    // underlying Set.
    // This means that we can only create new EnumerableSets for types that fit
    // in bytes32.

    struct Set {
        // Storage of set values
        bytes32[] _values;
        // Position is the index of the value in the `values` array plus 1.
        // Position 0 is used to mean a value is not in the set.
        mapping(bytes32 value => uint256) _positions;
    }

    /**
     * @dev Add a value to a set. O(1).
     *
     * Returns true if the value was added to the set, that is if it was not
     * already present.
     */
    function _add(Set storage set, bytes32 value) private returns (bool) {
        if (!_contains(set, value)) {
            set._values.push(value);
            // The value is stored at length-1, but we add 1 to all indexes
            // and use 0 as a sentinel value
            set._positions[value] = set._values.length;
            return true;
        } else {
            return false;
        }
    }

    /**
     * @dev Removes a value from a set. O(1).
     *
     * Returns true if the value was removed from the set, that is if it was
     * present.
     */
    function _remove(Set storage set, bytes32 value) private returns (bool) {
        // We cache the value's position to prevent multiple reads from the same storage slot
        uint256 position = set._positions[value];

        if (position != 0) {
            // Equivalent to contains(set, value)
            // To delete an element from the _values array in O(1), we swap the element to delete with the last one in
            // the array, and then remove the last element (sometimes called as 'swap and pop').
            // This modifies the order of the array, as noted in {at}.

            uint256 valueIndex = position - 1;
            uint256 lastIndex = set._values.length - 1;

            if (valueIndex != lastIndex) {
                bytes32 lastValue = set._values[lastIndex];

                // Move the lastValue to the index where the value to delete is
                set._values[valueIndex] = lastValue;
                // Update the tracked position of the lastValue (that was just moved)
                set._positions[lastValue] = position;
            }

            // Delete the slot where the moved value was stored
            set._values.pop();

            // Delete the tracked position for the deleted slot
            delete set._positions[value];

            return true;
        } else {
            return false;
        }
    }

    /**
     * @dev Returns true if the value is in the set. O(1).
     */
    function _contains(Set storage set, bytes32 value) private view returns (bool) {
        return set._positions[value] != 0;
    }

    /**
     * @dev Returns the number of values on the set. O(1).
     */
    function _length(Set storage set) private view returns (uint256) {
        return set._values.length;
    }

    /**
     * @dev Returns the value stored at position `index` in the set. O(1).
     *
     * Note that there are no guarantees on the ordering of values inside the
     * array, and it may change when more values are added or removed.
     *
     * Requirements:
     *
     * - `index` must be strictly less than {length}.
     */
    function _at(Set storage set, uint256 index) private view returns (bytes32) {
        return set._values[index];
    }

    /**
     * @dev Return the entire set in an array
     *
     * WARNING: This operation will copy the entire storage to memory, which can be quite expensive. This is designed
     * to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that
     * this function has an unbounded cost, and using it as part of a state-changing function may render the function
     * uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.
     */
    function _values(Set storage set) private view returns (bytes32[] memory) {
        return set._values;
    }

    // Bytes32Set

    struct Bytes32Set {
        Set _inner;
    }

    /**
     * @dev Add a value to a set. O(1).
     *
     * Returns true if the value was added to the set, that is if it was not
     * already present.
     */
    function add(Bytes32Set storage set, bytes32 value) internal returns (bool) {
        return _add(set._inner, value);
    }

    /**
     * @dev Removes a value from a set. O(1).
     *
     * Returns true if the value was removed from the set, that is if it was
     * present.
     */
    function remove(Bytes32Set storage set, bytes32 value) internal returns (bool) {
        return _remove(set._inner, value);
    }

    /**
     * @dev Returns true if the value is in the set. O(1).
     */
    function contains(Bytes32Set storage set, bytes32 value) internal view returns (bool) {
        return _contains(set._inner, value);
    }

    /**
     * @dev Returns the number of values in the set. O(1).
     */
    function length(Bytes32Set storage set) internal view returns (uint256) {
        return _length(set._inner);
    }

    /**
     * @dev Returns the value stored at position `index` in the set. O(1).
     *
     * Note that there are no guarantees on the ordering of values inside the
     * array, and it may change when more values are added or removed.
     *
     * Requirements:
     *
     * - `index` must be strictly less than {length}.
     */
    function at(Bytes32Set storage set, uint256 index) internal view returns (bytes32) {
        return _at(set._inner, index);
    }

    /**
     * @dev Return the entire set in an array
     *
     * WARNING: This operation will copy the entire storage to memory, which can be quite expensive. This is designed
     * to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that
     * this function has an unbounded cost, and using it as part of a state-changing function may render the function
     * uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.
     */
    function values(Bytes32Set storage set) internal view returns (bytes32[] memory) {
        bytes32[] memory store = _values(set._inner);
        bytes32[] memory result;

        /// @solidity memory-safe-assembly
        assembly {
            result := store
        }

        return result;
    }

    // AddressSet

    struct AddressSet {
        Set _inner;
    }

    /**
     * @dev Add a value to a set. O(1).
     *
     * Returns true if the value was added to the set, that is if it was not
     * already present.
     */
    function add(AddressSet storage set, address value) internal returns (bool) {
        return _add(set._inner, bytes32(uint256(uint160(value))));
    }

    /**
     * @dev Removes a value from a set. O(1).
     *
     * Returns true if the value was removed from the set, that is if it was
     * present.
     */
    function remove(AddressSet storage set, address value) internal returns (bool) {
        return _remove(set._inner, bytes32(uint256(uint160(value))));
    }

    /**
     * @dev Returns true if the value is in the set. O(1).
     */
    function contains(AddressSet storage set, address value) internal view returns (bool) {
        return _contains(set._inner, bytes32(uint256(uint160(value))));
    }

    /**
     * @dev Returns the number of values in the set. O(1).
     */
    function length(AddressSet storage set) internal view returns (uint256) {
        return _length(set._inner);
    }

    /**
     * @dev Returns the value stored at position `index` in the set. O(1).
     *
     * Note that there are no guarantees on the ordering of values inside the
     * array, and it may change when more values are added or removed.
     *
     * Requirements:
     *
     * - `index` must be strictly less than {length}.
     */
    function at(AddressSet storage set, uint256 index) internal view returns (address) {
        return address(uint160(uint256(_at(set._inner, index))));
    }

    /**
     * @dev Return the entire set in an array
     *
     * WARNING: This operation will copy the entire storage to memory, which can be quite expensive. This is designed
     * to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that
     * this function has an unbounded cost, and using it as part of a state-changing function may render the function
     * uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.
     */
    function values(AddressSet storage set) internal view returns (address[] memory) {
        bytes32[] memory store = _values(set._inner);
        address[] memory result;

        /// @solidity memory-safe-assembly
        assembly {
            result := store
        }

        return result;
    }

    // UintSet

    struct UintSet {
        Set _inner;
    }

    /**
     * @dev Add a value to a set. O(1).
     *
     * Returns true if the value was added to the set, that is if it was not
     * already present.
     */
    function add(UintSet storage set, uint256 value) internal returns (bool) {
        return _add(set._inner, bytes32(value));
    }

    /**
     * @dev Removes a value from a set. O(1).
     *
     * Returns true if the value was removed from the set, that is if it was
     * present.
     */
    function remove(UintSet storage set, uint256 value) internal returns (bool) {
        return _remove(set._inner, bytes32(value));
    }

    /**
     * @dev Returns true if the value is in the set. O(1).
     */
    function contains(UintSet storage set, uint256 value) internal view returns (bool) {
        return _contains(set._inner, bytes32(value));
    }

    /**
     * @dev Returns the number of values in the set. O(1).
     */
    function length(UintSet storage set) internal view returns (uint256) {
        return _length(set._inner);
    }

    /**
     * @dev Returns the value stored at position `index` in the set. O(1).
     *
     * Note that there are no guarantees on the ordering of values inside the
     * array, and it may change when more values are added or removed.
     *
     * Requirements:
     *
     * - `index` must be strictly less than {length}.
     */
    function at(UintSet storage set, uint256 index) internal view returns (uint256) {
        return uint256(_at(set._inner, index));
    }

    /**
     * @dev Return the entire set in an array
     *
     * WARNING: This operation will copy the entire storage to memory, which can be quite expensive. This is designed
     * to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that
     * this function has an unbounded cost, and using it as part of a state-changing function may render the function
     * uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.
     */
    function values(UintSet storage set) internal view returns (uint256[] memory) {
        bytes32[] memory store = _values(set._inner);
        uint256[] memory result;

        /// @solidity memory-safe-assembly
        assembly {
            result := store
        }

        return result;
    }
}

// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.20;

/**
 * @title Assertions
 * @notice This library contains assertions for common requirement checks
 */
library Assertions {
  // --- Errors ---

  /// @dev Throws if `_x` is not greater than `_y`
  error NotGreaterThan(uint256 _x, uint256 _y);
  /// @dev Throws if `_x` is not lesser than `_y`
  error NotLesserThan(uint256 _x, uint256 _y);
  /// @dev Throws if `_x` is not greater than or equal to `_y`
  error NotGreaterOrEqualThan(uint256 _x, uint256 _y);
  /// @dev Throws if `_x` is not lesser than or equal to `_y`
  error NotLesserOrEqualThan(uint256 _x, uint256 _y);
  /// @dev Throws if `_x` is not greater than `_y`
  error IntNotGreaterThan(int256 _x, int256 _y);
  /// @dev Throws if `_x` is not lesser than `_y`
  error IntNotLesserThan(int256 _x, int256 _y);
  /// @dev Throws if `_x` is not greater than or equal to `_y`
  error IntNotGreaterOrEqualThan(int256 _x, int256 _y);
  /// @dev Throws if `_x` is not lesser than or equal to `_y`
  error IntNotLesserOrEqualThan(int256 _x, int256 _y);
  /// @dev Throws if checked amount is null
  error NullAmount();
  /// @dev Throws if checked address is null
  error NullAddress();
  /// @dev Throws if checked address contains no code
  error NoCode(address _contract);

  // --- Assertions ---

  /// @dev Asserts that `_x` is greater than `_y` and returns `_x`
  function assertGt(uint256 _x, uint256 _y) internal pure returns (uint256 __x) {
    if (_x <= _y) revert NotGreaterThan(_x, _y);
    return _x;
  }

  /// @dev Asserts that `_x` is greater than `_y` and returns `_x`
  function assertGt(int256 _x, int256 _y) internal pure returns (int256 __x) {
    if (_x <= _y) revert IntNotGreaterThan(_x, _y);
    return _x;
  }

  /// @dev Asserts that `_x` is greater than or equal to `_y` and returns `_x`
  function assertGtEq(uint256 _x, uint256 _y) internal pure returns (uint256 __x) {
    if (_x < _y) revert NotGreaterOrEqualThan(_x, _y);
    return _x;
  }

  /// @dev Asserts that `_x` is greater than or equal to `_y` and returns `_x`
  function assertGtEq(int256 _x, int256 _y) internal pure returns (int256 __x) {
    if (_x < _y) revert IntNotGreaterOrEqualThan(_x, _y);
    return _x;
  }

  /// @dev Asserts that `_x` is lesser than `_y` and returns `_x`
  function assertLt(uint256 _x, uint256 _y) internal pure returns (uint256 __x) {
    if (_x >= _y) revert NotLesserThan(_x, _y);
    return _x;
  }

  /// @dev Asserts that `_x` is lesser than `_y` and returns `_x`
  function assertLt(int256 _x, int256 _y) internal pure returns (int256 __x) {
    if (_x >= _y) revert IntNotLesserThan(_x, _y);
    return _x;
  }

  /// @dev Asserts that `_x` is lesser than or equal to `_y` and returns `_x`
  function assertLtEq(uint256 _x, uint256 _y) internal pure returns (uint256 __x) {
    if (_x > _y) revert NotLesserOrEqualThan(_x, _y);
    return _x;
  }

  /// @dev Asserts that `_x` is lesser than or equal to `_y` and returns `_x`
  function assertLtEq(int256 _x, int256 _y) internal pure returns (int256 __x) {
    if (_x > _y) revert IntNotLesserOrEqualThan(_x, _y);
    return _x;
  }

  /// @dev Asserts that `_x` is not null and returns `_x`
  function assertNonNull(uint256 _x) internal pure returns (uint256 __x) {
    if (_x == 0) revert NullAmount();
    return _x;
  }

  /// @dev Asserts that `_address` is not null and returns `_address`
  function assertNonNull(address _address) internal pure returns (address __address) {
    if (_address == address(0)) revert NullAddress();
    return _address;
  }

  /// @dev Asserts that `_address` contains code and returns `_address`
  function assertHasCode(address _address) internal view returns (address __address) {
    if (_address.code.length == 0) revert NoCode(_address);
    return _address;
  }
}

// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.20;

interface IHaiSafeManager {
  // --- Events ---

  /// @notice Emitted when calling allowSAFE with the sender address and the method arguments
  event AllowSAFE(address indexed _sender, uint256 indexed _safe, address _usr, bool _ok);
  /// @notice Emitted when calling allowHandler with the sender address and the method arguments
  event AllowHandler(address indexed _sender, address _usr, bool _ok);
  /// @notice Emitted when calling initiateTransferSAFEOwnership with the sender address and the method arguments
  event InitiateTransferSAFEOwnership(address indexed _sender, uint256 indexed _safe, address _dst);
  /// @notice Emitted when calling transferSAFEOwnership with the sender address and the method arguments
  event TransferSAFEOwnership(address indexed _sender, uint256 indexed _safe, address _dst);
  /// @notice Emitted when calling openSAFE with the sender address and the method arguments
  event OpenSAFE(address indexed _sender, address indexed _own, uint256 indexed _safe);
  /// @notice Emitted when calling modifySAFECollateralization with the sender address and the method arguments
  event ModifySAFECollateralization(
    address indexed _sender, uint256 indexed _safe, int256 _deltaCollateral, int256 _deltaDebt
  );
  /// @notice Emitted when calling transferCollateral with the sender address and the method arguments
  event TransferCollateral(address indexed _sender, uint256 indexed _safe, address _dst, uint256 _wad);
  /// @notice Emitted when calling transferCollateral (specifying cType) with the sender address and the method arguments
  event TransferCollateral(address indexed _sender, bytes32 _cType, uint256 indexed _safe, address _dst, uint256 _wad);
  /// @notice Emitted when calling transferInternalCoins with the sender address and the method arguments
  event TransferInternalCoins(address indexed _sender, uint256 indexed _safe, address _dst, uint256 _rad);
  /// @notice Emitted when calling quitSystem with the sender address and the method arguments
  event QuitSystem(address indexed _sender, uint256 indexed _safe, address _dst);
  /// @notice Emitted when calling enterSystem with the sender address and the method arguments
  event EnterSystem(address indexed _sender, address _src, uint256 indexed _safe);
  /// @notice Emitted when calling moveSAFE with the sender address and the method arguments
  event MoveSAFE(address indexed _sender, uint256 indexed _safeSrc, uint256 indexed _safeDst);
  /// @notice Emitted when calling protectSAFE with the sender address and the method arguments
  event ProtectSAFE(address indexed _sender, uint256 indexed _safe, address _liquidationEngine, address _saviour);

  // --- Errors ---

  /// @notice Throws if the provided address is null
  error ZeroAddress();
  /// @notice Throws when trying to call a function not allowed for a given safe
  error SafeNotAllowed();
  /// @notice Throws when trying to call a function not allowed for a given handler
  error HandlerNotAllowed();
  /// @notice Throws when trying to transfer safe ownership to the current owner
  error AlreadySafeOwner();
  /// @notice Throws when trying to move a safe to another one with different collateral type
  error CollateralTypesMismatch();

  // --- Structs ---

  struct SAFEData {
    // Address of the safe owner
    address owner;
    // Address of the safe owner pending to be set
    address pendingOwner;
    // Address of the safe handler
    address safeHandler;
    // Collateral type of the safe
    bytes32 collateralType;
  }

  // --- Data ---

  /// @notice Address of the SAFEEngine
  function safeEngine() external view returns (address _safeEngine);

  /// @notice Mapping of owner and safe permissions to a caller permissions
  function safeCan(address _owner, uint256 _safeId, address _caller) external view returns (bool _ok);

  /// @notice Mapping of handler to a caller permissions
  function handlerCan(address _safeHandler, address _caller) external view returns (bool _ok);

  // --- Getters ---

  /**
   * @notice Getter for the list of safes owned by a user
   * @param  _usr Address of the user
   * @return _safes List of safe ids owned by the user
   */
  function getSafes(address _usr) external view returns (uint256[] memory _safes);

  /**
   * @notice Getter for the list of safes owned by a user for a given collateral type
   * @param  _usr Address of the user
   * @param  _cType Bytes32 representation of the collateral type
   * @return _safes List of safe ids owned by the user for the given collateral type
   */
  function getSafes(address _usr, bytes32 _cType) external view returns (uint256[] memory _safes);

  /**
   * @notice Getter for the details of the safes owned by a user
   * @param  _usr Address of the user
   * @return _safes List of safe ids owned by the user
   * @return _safeHandlers List of safe handlers addresses owned by the user
   * @return _cTypes List of collateral types of the safes owned by the user
   */
  function getSafesData(address _usr)
    external
    view
    returns (uint256[] memory _safes, address[] memory _safeHandlers, bytes32[] memory _cTypes);

  /**
   * @notice Getter for the details of a SAFE
   * @param  _safe Id of the SAFE
   * @return _sData Struct with the safe data
   */
  function safeData(uint256 _safe) external view returns (SAFEData memory _sData);

  // --- Methods ---

  /**
   * @notice Allow/disallow a user address to manage the safe
   * @param  _safe Id of the SAFE
   * @param  _usr Address of the user to allow/disallow
   * @param  _ok Boolean state to allow/disallow
   */
  function allowSAFE(uint256 _safe, address _usr, bool _ok) external;

  /**
   * @notice Allow/disallow a handler address to manage the safe
   * @param  _usr Address of the user to allow/disallow
   * @param  _ok Boolean state to allow/disallow
   */
  function allowHandler(address _usr, bool _ok) external;

  /**
   * @notice Open a new safe for a user address
   * @param  _cType Bytes32 representation of the collateral type
   * @param  _usr Address of the user to open the safe for
   * @return _id Id of the new SAFE
   */
  function openSAFE(bytes32 _cType, address _usr) external returns (uint256 _id);

  /**
   * @notice Initiate the transfer of the ownership of a safe to a dst address
   * @param  _safe Id of the SAFE
   * @param  _dst Address of the dst address
   */
  function transferSAFEOwnership(uint256 _safe, address _dst) external;

  /**
   * @notice Accept the transfer of the ownership of a safe
   * @param  _safe Id of the SAFE
   */
  function acceptSAFEOwnership(uint256 _safe) external;

  /**
   * @notice Modify a SAFE's collateralization ratio while keeping the generated COIN or collateral freed in the safe handler address
   * @param  _safe Id of the SAFE
   * @param  _deltaCollateral Delta of collateral to add/remove [wad]
   * @param  _deltaDebt Delta of debt to add/remove [wad]
   */
  function modifySAFECollateralization(uint256 _safe, int256 _deltaCollateral, int256 _deltaDebt) external;

  /**
   * @notice Transfer wad amount of safe collateral from the safe address to a dst address
   * @param  _safe Id of the SAFE
   * @param  _dst Address of the dst address
   * @param  _wad Amount of collateral to transfer [wad]
   */
  function transferCollateral(uint256 _safe, address _dst, uint256 _wad) external;

  /**
   * @notice Transfer wad amount of any type of collateral from the safe address to a dst address
   * @param  _cType Bytes32 representation of the collateral type
   * @param  _safe Id of the SAFE
   * @param  _dst Address of the dst address
   * @param  _wad Amount of collateral to transfer [wad]
   * @dev    This function has the purpose to take away collateral from the system that doesn't correspond to the safe but was sent there wrongly.
   */
  function transferCollateral(bytes32 _cType, uint256 _safe, address _dst, uint256 _wad) external;

  /**
   * @notice Transfer an amount of COIN from the safe address to a dst address [rad]
   * @param  _safe Id of the SAFE
   * @param  _dst Address of the dst address
   * @param  _rad Amount of COIN to transfer [rad]
   */
  function transferInternalCoins(uint256 _safe, address _dst, uint256 _rad) external;

  /**
   * @notice Quit the system, migrating the safe (lockedCollateral, generatedDebt) to a different dst handler
   * @param  _safe Id of the SAFE
   * @param  _dst Address of the dst handler
   */
  function quitSystem(uint256 _safe, address _dst) external;

  /**
   * @notice Enter the system, migrating the safe (lockedCollateral, generatedDebt) from a src handler to the safe handler
   * @param  _src Address of the src handler
   * @param  _safe Id of the SAFE
   */
  function enterSystem(address _src, uint256 _safe) external;

  /**
   * @notice Move a position from safeSrc handler to the safeDst handler
   * @param  _safeSrc Id of the source SAFE
   * @param  _safeDst Id of the destination SAFE
   */
  function moveSAFE(uint256 _safeSrc, uint256 _safeDst) external;

  /**
   * @notice Add a safe to the user's list of safes (doesn't set safe ownership)
   * @param  _safe Id of the SAFE
   * @dev    This function is meant to allow the user to add a safe to their list (if it was previously removed)
   */
  function addSAFE(uint256 _safe) external;

  /**
   * @notice Remove a safe from the user's list of safes (doesn't erase safe ownership)
   * @param  _safe Id of the SAFE
   * @dev    This function is meant to allow the user to remove a safe from their list (if it was added against their will)
   */
  function removeSAFE(uint256 _safe) external;

  /**
   * @notice Choose a safe saviour inside LiquidationEngine for the SAFE
   * @param  _safe Id of the SAFE
   * @param  _liquidationEngine Address of the LiquidationEngine
   * @param  _saviour Address of the saviour
   */
  function protectSAFE(uint256 _safe, address _liquidationEngine, address _saviour) external;
}

// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.20;

interface IAuthorizable {
  // --- Events ---

  /**
   * @notice Emitted when an account is authorized
   * @param _account Account that is authorized
   */
  event AddAuthorization(address _account);

  /**
   * @notice Emitted when an account is unauthorized
   * @param _account Account that is unauthorized
   */
  event RemoveAuthorization(address _account);

  // --- Errors ---
  /// @notice Throws if the account is already authorized on `addAuthorization`
  error AlreadyAuthorized();
  /// @notice Throws if the account is not authorized on `removeAuthorization`
  error NotAuthorized();
  /// @notice Throws if the account is not authorized and tries to call an `onlyAuthorized` method
  error Unauthorized();

  // --- Data ---

  /**
   * @notice Checks whether an account is authorized on the contract
   * @param  _account Account to check
   * @return _authorized Whether the account is authorized or not
   */
  function authorizedAccounts(address _account) external view returns (bool _authorized);

  /**
   * @notice Getter for the authorized accounts
   * @return _accounts Array of authorized accounts
   */
  function authorizedAccounts() external view returns (address[] memory _accounts);

  // --- Administration ---

  /**
   * @notice Add authorization to an account
   * @param  _account Account to add authorization to
   * @dev    Method will revert if the account is already authorized
   */
  function addAuthorization(address _account) external;

  /**
   * @notice Remove authorization from an account
   * @param  _account Account to remove authorization from
   * @dev    Method will revert if the account is not authorized
   */
  function removeAuthorization(address _account) external;
}

// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.20;

import {IAuthorizable} from '@interfaces/utils/IAuthorizable.sol';

interface IModifiable is IAuthorizable {
  // --- Events ---
  /// @dev Event topic 1 is always a parameter, topic 2 can be empty (global params)
  event ModifyParameters(bytes32 indexed _param, bytes32 indexed _cType, bytes _data);

  // --- Errors ---
  error UnrecognizedParam();
  error UnrecognizedCType();

  // --- Administration ---
  /**
   * @notice Set a new value for a global specific parameter
   * @param _param String identifier of the parameter to modify
   * @param _data Encoded data to modify the parameter
   */
  function modifyParameters(bytes32 _param, bytes memory _data) external;
}

// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.20;

import {IAuthorizable} from '@interfaces/utils/IAuthorizable.sol';
import {IModifiable} from '@interfaces/utils/IModifiable.sol';

interface IModifiablePerCollateral is IAuthorizable, IModifiable {
  // --- Events ---
  /**
   * @notice Emitted when a new collateral type is registered
   * @param _cType Bytes32 representation of the collateral type
   */
  event InitializeCollateralType(bytes32 _cType);

  // --- Errors ---

  error CollateralTypeAlreadyInitialized();

  // --- Views ---

  /**
   * @notice List of all the collateral types registered in the OracleRelayer
   * @return __collateralList Array of all the collateral types registered
   */
  function collateralList() external view returns (bytes32[] memory __collateralList);

  // --- Methods ---

  /**
   * @notice Register a new collateral type in the SAFEEngine
   * @param _cType Collateral type to register
   * @param _collateralParams Collateral parameters
   */
  function initializeCollateralType(bytes32 _cType, bytes memory _collateralParams) external;

  /**
   * @notice Set a new value for a collateral specific parameter
   * @param _cType String identifier of the collateral to modify
   * @param _param String identifier of the parameter to modify
   * @param _data Encoded data to modify the parameter
   */
  function modifyParameters(bytes32 _cType, bytes32 _param, bytes memory _data) external;
}

// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.20;

import {IAuthorizable} from '@interfaces/utils/IAuthorizable.sol';

interface IDisableable is IAuthorizable {
  // --- Events ---

  /// @notice Emitted when the inheriting contract is disabled
  event DisableContract();

  // --- Errors ---

  /// @notice Throws when trying to call a `whenDisabled` method when the contract is enabled
  error ContractIsEnabled();
  /// @notice Throws when trying to call a `whenEnabled` method when the contract is disabled
  error ContractIsDisabled();
  /// @notice Throws when trying to disable a contract that cannot be disabled
  error NonDisableable();

  // --- Data ---

  /**
   * @notice Check if the contract is enabled
   * @return _contractEnabled True if the contract is enabled
   */
  function contractEnabled() external view returns (bool _contractEnabled);

  // --- Methods ---

  /**
   * @notice External method to trigger the contract disablement
   * @dev    Triggers an internal call to `_onContractDisable` virtual method
   */
  function disableContract() external;
}

// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.20;

import {ISAFEEngine} from '@interfaces/ISAFEEngine.sol';
import {ISurplusAuctionHouse} from '@interfaces/ISurplusAuctionHouse.sol';
import {IDebtAuctionHouse} from '@interfaces/IDebtAuctionHouse.sol';
import {IAuthorizable} from '@interfaces/utils/IAuthorizable.sol';
import {IModifiable} from '@interfaces/utils/IModifiable.sol';
import {IDisableable} from '@interfaces/utils/IDisableable.sol';

interface IAccountingEngine is IAuthorizable, IDisableable, IModifiable {
  // --- Events ---

  /**
   * @notice Emitted when a block of debt is pushed to the debt queue
   * @param _timestamp Timestamp of the block of debt that was pushed
   * @param _debtAmount Amount of debt that was pushed [rad]
   */
  event PushDebtToQueue(uint256 indexed _timestamp, uint256 _debtAmount);

  /**
   * @notice Emitted when a block of debt is popped from the debt queue
   * @param _timestamp Timestamp of the block of debt that was popped
   * @param _debtAmount Amount of debt that was popped [rad]
   */
  event PopDebtFromQueue(uint256 indexed _timestamp, uint256 _debtAmount);

  /**
   * @notice Emitted when the contract destroys an equal amount of coins and debt
   * @param _rad Amount of coins & debt that was destroyed [rad]
   * @param _coinBalance Amount of coins that remains after debt settlement [rad]
   * @param _debtBalance Amount of debt that remains after debt settlement [rad]
   */
  event SettleDebt(uint256 _rad, uint256 _coinBalance, uint256 _debtBalance);

  /**
   * @notice Emitted when the contract destroys an equal amount of coins and debt with surplus
   * @dev    Normally called with coins received from the DebtAuctionHouse
   * @param _rad Amount of coins & debt that was destroyed with surplus [rad]
   * @param _coinBalance Amount of coins that remains after debt settlement [rad]
   * @param _debtBalance Amount of debt that remains after debt settlement [rad]
   */
  event CancelDebt(uint256 _rad, uint256 _coinBalance, uint256 _debtBalance);

  /**
   * @notice Emitted when a debt auction is started
   * @param _id Id of the debt auction that was started
   * @param _initialBid Amount of protocol tokens that are initially offered in the debt auction [wad]
   * @param _debtAuctioned Amount of debt that is being auctioned [rad]
   */
  event AuctionDebt(uint256 indexed _id, uint256 _initialBid, uint256 _debtAuctioned);

  /**
   * @notice Emitted when a surplus auction is started
   * @param _id Id of the surplus auction that was started
   * @param _initialBid Amount of protocol tokens that are initially bidded in the surplus auction [wad]
   * @param _surplusAuctioned Amount of surplus that is being auctioned [rad]
   */
  event AuctionSurplus(uint256 indexed _id, uint256 _initialBid, uint256 _surplusAuctioned);

  /**
   * @notice Emitted when surplus is transferred to an address
   * @param _extraSurplusReceiver Address that received the surplus
   * @param _surplusTransferred Amount of surplus that was transferred [rad]
   */
  event TransferSurplus(address indexed _extraSurplusReceiver, uint256 _surplusTransferred);

  // --- Errors ---

  /// @notice Throws when trying to auction debt when it is disabled
  error AccEng_DebtAuctionDisabled();
  /// @notice Throws when trying to auction surplus when it is disabled
  error AccEng_SurplusAuctionDisabled();
  /// @notice Throws when trying to transfer surplus when it is disabled
  error AccEng_SurplusTransferDisabled();
  /// @notice Throws when trying to settle debt when there is not enough debt left to settle
  error AccEng_InsufficientDebt();
  /// @notice Throws when trying to auction / transfer surplus when there is not enough surplus
  error AccEng_InsufficientSurplus();
  /// @notice Throws when trying to push / pop / auction a null amount of debt / surplus
  error AccEng_NullAmount();
  /// @notice Throws when trying to transfer surplus to a null address
  error AccEng_NullSurplusReceiver();
  /// @notice Throws when trying to auction / transfer surplus before the cooldown has passed
  error AccEng_SurplusCooldown();
  /// @notice Throws when trying to pop debt before the cooldown has passed
  error AccEng_PopDebtCooldown();
  /// @notice Throws when trying to transfer post-settlement surplus before the disable cooldown has passed
  error AccEng_PostSettlementCooldown();

  // --- Structs ---

  struct AccountingEngineParams {
    // Whether the system transfers surplus instead of auctioning it
    uint256 /* 0 | 1  */ surplusIsTransferred;
    // Amount of seconds required to wait between surplus actions
    uint256 /* seconds */ surplusDelay;
    // Amount of seconds after which debt can be popped from debtQueue
    uint256 /* seconds */ popDebtDelay;
    // Amount of seconds to wait (post settlement) until surplus can be drained
    uint256 /* seconds */ disableCooldown;
    // Amount of surplus transferred or sold in one surplus action
    uint256 /* RAD     */ surplusAmount;
    // Amount of surplus that needs to accrue in this contract before any surplus action can start
    uint256 /* RAD     */ surplusBuffer;
    // Amount of protocol tokens offered to be minted in debt auctions
    uint256 /* WAD     */ debtAuctionMintedTokens;
    // Amount of debt sold in one debt auction
    uint256 /* RAD     */ debtAuctionBidSize;
  }

  // --- Registry ---

  /// @notice Address of the SAFEEngine contract
  function safeEngine() external view returns (ISAFEEngine _safeEngine);

  /// @notice Address of the SurplusAuctionHouse contract
  function surplusAuctionHouse() external view returns (ISurplusAuctionHouse _surplusAuctionHouse);

  /// @notice Address of the DebtAuctionHouse contract
  function debtAuctionHouse() external view returns (IDebtAuctionHouse _debtAuctionHouse);

  /**
   * @notice The post settlement surplus drain is used to transfer remaining surplus after settlement is triggered
   * @dev    Usually the `SettlementSurplusAuctioneer` contract
   * @return _postSettlementSurplusDrain Address of the contract that handles post settlement surplus
   */
  function postSettlementSurplusDrain() external view returns (address _postSettlementSurplusDrain);

  /**
   * @notice The extra surplus receiver is used to transfer surplus if is not being auctioned
   * @return _extraSurplusReceiver Address of the contract that handles extra surplus transfers
   */
  function extraSurplusReceiver() external view returns (address _extraSurplusReceiver);

  // --- Params ---

  /**
   * @notice Getter for the contract parameters struct
   * @return _params AccountingEngine parameters struct
   */
  function params() external view returns (AccountingEngineParams memory _params);

  /**
   * @notice Getter for the unpacked contract parameters struct
   * @return _surplusIsTransferred Whether the system transfers surplus instead of auctioning it [0/1]
   * @return _surplusDelay Amount of seconds between surplus actions
   * @return _popDebtDelay Amount of seconds after which debt can be popped from debtQueue
   * @return _disableCooldown Amount of seconds to wait (post settlement) until surplus can be drained
   * @return _surplusAmount Amount of surplus transferred or sold in one surplus action [rad]
   * @return _surplusBuffer Amount of surplus that needs to accrue in this contract before any surplus action can start [rad]
   * @return _debtAuctionMintedTokens Amount of protocol tokens to be minted in debt auctions [wad]
   * @return _debtAuctionBidSize Amount of debt sold in one debt auction [rad]
   */
  // solhint-disable-next-line private-vars-leading-underscore
  function _params()
    external
    view
    returns (
      uint256 _surplusIsTransferred,
      uint256 _surplusDelay,
      uint256 _popDebtDelay,
      uint256 _disableCooldown,
      uint256 _surplusAmount,
      uint256 _surplusBuffer,
      uint256 _debtAuctionMintedTokens,
      uint256 _debtAuctionBidSize
    );

  // --- Data ---

  /**
   * @notice The total amount of debt that is currently on auction in the `DebtAuctionHouse`
   * @return _totalOnAuctionDebt Total amount of debt that is currently on auction [rad]
   */
  function totalOnAuctionDebt() external view returns (uint256 _totalOnAuctionDebt);

  /**
   * @notice A mapping storing debtBlocks that need to be covered by auctions
   * @dev    A debtBlock can be popped from the queue (to be auctioned) if more than `popDebtDelay` has elapsed since creation
   * @param  _blockTimestamp The timestamp of the debtBlock
   * @return _debtBlock The amount of debt created in the inputted blockTimestamp [rad]
   */
  function debtQueue(uint256 _blockTimestamp) external view returns (uint256 _debtBlock);

  /**
   * @notice The total amount of debt that is currently in the debtQueue to be auctioned
   * @return _totalQueuedDebt Total amount of debt in RAD that is currently in the debtQueue [rad]
   */
  function totalQueuedDebt() external view returns (uint256 _totalQueuedDebt);

  /**
   * @notice The timestamp of the last time surplus was transferred or auctioned
   * @return _lastSurplusTime Timestamp of when the last surplus transfer or auction was triggered
   */
  function lastSurplusTime() external view returns (uint256 _lastSurplusTime);

  /**
   * @notice Returns the amount of bad debt that is not in the debtQueue and is not currently handled by debt auctions
   * @return _unqueuedUnauctionedDebt Amount of debt in RAD that is currently not in the debtQueue and not on auction [rad]
   * @dev    The difference between the debt in the SAFEEngine and the debt in the debtQueue and on auction
   */
  function unqueuedUnauctionedDebt() external view returns (uint256 _unqueuedUnauctionedDebt);

  /**
   * @dev    When the contract is disabled (usually by `GlobalSettlement`) it has to wait `disableCooldown`
   *         before any remaining surplus can be transferred to `postSettlementSurplusDrain`
   * @return _disableTimestamp Timestamp of when the contract was disabled
   */
  function disableTimestamp() external view returns (uint256 _disableTimestamp);

  // --- Methods ---

  /**
   * @notice Push a block of debt to the debt queue
   * @dev    Usually called by the `LiquidationEngine` when a SAFE is liquidated
   * @dev    Debt is locked in a queue to give the system enough time to auction collateral
   *         and gather surplus
   * @param  _debtBlock Amount of debt to push [rad]
   */
  function pushDebtToQueue(uint256 _debtBlock) external;

  /**
   * @notice Pop a block of debt from the debt queue
   * @dev    A debtBlock can be popped from the queue after `popDebtDelay` seconds have passed since creation
   * @param  _debtBlockTimestamp Timestamp of the block of debt that should be popped out
   */
  function popDebtFromQueue(uint256 _debtBlockTimestamp) external;

  /**
   * @notice Destroy an equal amount of coins and debt
   * @dev    It can only destroy debt that is not locked in the queue and also not in a debt auction (`unqueuedUnauctionedDebt`)
   * @param _rad Amount of coins & debt to destroy [rad]
   */
  function settleDebt(uint256 _rad) external;

  /**
   * @notice Use surplus coins to destroy debt that was in a debt auction
   * @dev    Usually called by the `DebtAuctionHouse` after a debt bid is made
   * @param _rad Amount of coins & debt to destroy with surplus [rad]
   */
  function cancelAuctionedDebtWithSurplus(uint256 _rad) external;

  /**
   * @notice Start a debt auction (print protocol tokens in exchange for coins so that the system can be recapitalized)
   * @dev    It can only auction debt that has been popped from the debt queue and is not already being auctioned
   * @return _id Id of the debt auction that was started
   */
  function auctionDebt() external returns (uint256 _id);

  /**
   * @notice Start a surplus auction (sell surplus stability fees for protocol tokens)
   * @dev    It can only auction surplus if `surplusIsTransferred` is set to false
   * @dev    It can only auction surplus if `surplusDelay` seconds have elapsed since the last surplus auction/transfer was triggered
   * @dev    It can only auction surplus if enough surplus remains in the buffer and if there is no more debt left to settle
   * @return _id Id of the surplus auction that was started
   */
  function auctionSurplus() external returns (uint256 _id);

  /**
   * @notice Transfer surplus to an address as an alternative to surplus auctions
   * @dev    It can only transfer surplus if `surplusIsTransferred` is set to true
   * @dev    It can only transfer surplus if `surplusDelay` seconds have elapsed since the last surplus auction/transfer was triggered
   * @dev    It can only transfer surplus if enough surplus remains in the buffer and if there is no more debt left to settle
   */
  function transferExtraSurplus() external;

  /**
   * @notice Transfer any remaining surplus after the disable cooldown has passed. Meant to be a backup in case GlobalSettlement.processSAFE
   *         has a bug, governance doesn't have power over the system and there's still surplus left in the AccountingEngine
   *         which then blocks GlobalSettlement.setOutstandingCoinSupply.
   * @dev    Transfer any remaining surplus after `disableCooldown` seconds have passed since disabling the contract
   */
  function transferPostSettlementSurplus() external;
}

// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.20;

import {ICommonSurplusAuctionHouse} from '@interfaces/ICommonSurplusAuctionHouse.sol';

import {IAuthorizable} from '@interfaces/utils/IAuthorizable.sol';
import {IModifiable} from '@interfaces/utils/IModifiable.sol';
import {IDisableable} from '@interfaces/utils/IDisableable.sol';

interface ISurplusAuctionHouse is IAuthorizable, IDisableable, IModifiable, ICommonSurplusAuctionHouse {
  // --- Events ---

  /**
   * @notice Emitted when an auction is prematurely terminated
   * @param  _id Id of the auction
   * @param  _blockTimestamp Time when the auction was terminated
   * @param  _highBidder Who won the auction
   * @param  _raisedAmount Amount of protocol tokens raised in the auction [rad]
   */
  event TerminateAuctionPrematurely(
    uint256 indexed _id, uint256 _blockTimestamp, address _highBidder, uint256 _raisedAmount
  );

  // --- Errors ---

  /// @notice Throws when trying to start an auction with non-zero recycling percentage and null bid receiver
  error SAH_NullProtTokenReceiver();

  struct SurplusAuctionHouseParams {
    // Minimum bid increase compared to the last bid in order to take the new one in consideration
    uint256 /* WAD %   */ bidIncrease;
    // How long the auction lasts after a new bid is submitted
    uint256 /* seconds */ bidDuration;
    // Total length of the auction
    uint256 /* seconds */ totalAuctionLength;
    // Receiver of protocol tokens
    address /*         */ bidReceiver;
    // Percentage of protocol tokens to recycle
    uint256 /* WAD %   */ recyclingPercentage;
  }

  // --- Params ---

  /**
   * @notice Getter for the contract parameters struct
   * @return _sahParams Auction house parameters struct
   */
  function params() external view returns (SurplusAuctionHouseParams memory _sahParams);

  /**
   * @notice Getter for the unpacked contract parameters struct
   * @return _bidIncrease Minimum bid increase compared to the last bid in order to take the new one in consideration [wad %]
   * @return _bidDuration How long the auction lasts after a new bid is submitted [seconds]
   * @return _totalAuctionLength Total length of the auction [seconds]
   * @return _bidReceiver Receiver of protocol tokens
   * @return _recyclingPercentage Percentage of protocol tokens to recycle [wad %]
   */
  // solhint-disable-next-line private-vars-leading-underscore
  function _params()
    external
    view
    returns (
      uint256 _bidIncrease,
      uint256 _bidDuration,
      uint256 _totalAuctionLength,
      address _bidReceiver,
      uint256 _recyclingPercentage
    );

  /**
   * @notice Terminate an auction prematurely.
   * @param  _id ID of the auction to settle/terminate
   */
  function terminateAuctionPrematurely(uint256 _id) external;
}

// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.20;

import {ISAFEEngine} from '@interfaces/ISAFEEngine.sol';
import {IAccountingEngine} from '@interfaces/IAccountingEngine.sol';
import {IProtocolToken} from '@interfaces/tokens/IProtocolToken.sol';

import {IAuthorizable} from '@interfaces/utils/IAuthorizable.sol';
import {IModifiable} from '@interfaces/utils/IModifiable.sol';
import {IDisableable} from '@interfaces/utils/IDisableable.sol';

interface IDebtAuctionHouse is IAuthorizable, IDisableable, IModifiable {
  // --- Events ---

  /**
   * @notice Emitted when a new auction is started
   * @param  _id Id of the auction
   * @param  _auctioneer Address who started the auction
   * @param  _blockTimestamp Time when the auction was started
   * @param  _amountToSell How much protocol tokens are initially offered [wad]
   * @param  _amountToRaise Amount of system coins to raise [rad]
   * @param  _auctionDeadline Time when the auction expires
   */
  event StartAuction(
    uint256 indexed _id,
    address indexed _auctioneer,
    uint256 _blockTimestamp,
    uint256 _amountToSell,
    uint256 _amountToRaise,
    uint256 _auctionDeadline
  );

  /**
   * @notice Emitted when an auction is restarted
   * @param  _id Id of the auction
   * @param  _blockTimestamp Time when the auction was restarted
   * @param  _auctionDeadline New time when the auction expires
   */
  event RestartAuction(uint256 indexed _id, uint256 _blockTimestamp, uint256 _auctionDeadline);

  /**
   * @notice Emitted when a bid is made in an auction
   * @param  _id Id of the auction
   * @param  _bidder Who made the bid
   * @param  _blockTimestamp Time when the bid was made
   * @param  _raisedAmount Amount of system coins raised in the bid [rad]
   * @param  _soldAmount Amount of protocol tokens offered to buy in the bid [wad]
   * @param  _bidExpiry Time when the bid expires
   */
  event DecreaseSoldAmount(
    uint256 indexed _id,
    address _bidder,
    uint256 _blockTimestamp,
    uint256 _raisedAmount,
    uint256 _soldAmount,
    uint256 _bidExpiry
  );

  /**
   * @notice Emitted when an auction is settled
   * @dev    An auction is settled after the winning bid or the auction expire
   * @param  _id Id of the auction
   * @param  _blockTimestamp Time when the auction was settled
   * @param  _highBidder Who won the auction
   * @param  _raisedAmount Amount of system coins raised in the auction [rad]
   */
  event SettleAuction(uint256 indexed _id, uint256 _blockTimestamp, address _highBidder, uint256 _raisedAmount);

  /**
   * @notice Emitted when an auction is terminated prematurely
   * @param  _id Id of the auction
   * @param  _blockTimestamp Time when the auction was terminated
   * @param  _highBidder Who won the auction
   * @param  _raisedAmount Amount of system coins raised in the auction [rad]
   */
  event TerminateAuctionPrematurely(
    uint256 indexed _id, uint256 _blockTimestamp, address _highBidder, uint256 _raisedAmount
  );

  // --- Errors ---

  /// @dev Throws when trying to restart an auction that never started
  error DAH_AuctionNeverStarted();
  /// @dev Throws when trying to restart an auction that is still active
  error DAH_AuctionNotFinished();
  /// @dev Throws when trying to restart an auction that already has a winning bid
  error DAH_BidAlreadyPlaced();
  /// @dev Throws when trying to bid in an auction that already has expired
  error DAH_AuctionAlreadyExpired();
  /// @dev Throws when trying to bid in an auction that has a bid already expired
  error DAH_BidAlreadyExpired();
  /// @dev Throws when trying to bid in an auction with a bid that doesn't match the current bid
  error DAH_NotMatchingBid();
  /// @dev Throws when trying to place a bid that is not lower than the current bid
  error DAH_AmountBoughtNotLower();
  /// @dev Throws when trying to place a bid not lower than the current bid threshold
  error DAH_InsufficientDecrease();
  /// @dev Throws when prematurely terminating an auction that has no bids
  error DAH_HighBidderNotSet();

  // --- Data ---

  struct Auction {
    // Bid size
    uint256 /* RAD  */ bidAmount;
    // How many protocol tokens are sold in an auction
    uint256 /* WAD  */ amountToSell;
    // Who the high bidder is
    address /*      */ highBidder;
    // When the latest bid expires and the auction can be settled
    uint256 /* unix */ bidExpiry;
    // Hard deadline for the auction after which no more bids can be placed
    uint256 /* unix */ auctionDeadline;
  }

  struct DebtAuctionHouseParams {
    // Minimum bid increase compared to the last bid in order to take the new one in consideration
    uint256 /* WAD %   */ bidDecrease;
    // Increase in protocol tokens sold in case an auction is restarted
    uint256 /* WAD %   */ amountSoldIncrease;
    // How long the auction lasts after a new bid is submitted
    uint256 /* seconds */ bidDuration;
    // Total length of the auction
    uint256 /* seconds */ totalAuctionLength;
  }

  /**
   * @notice Type of the auction house
   * @return _auctionHouseType Bytes32 representation of the auction house type
   */
  // solhint-disable-next-line func-name-mixedcase
  function AUCTION_HOUSE_TYPE() external view returns (bytes32 _auctionHouseType);

  /**
   * @notice Data of an auction
   * @param  _id Id of the auction
   * @return _auction Auction data struct
   */
  function auctions(uint256 _id) external view returns (Auction memory _auction);

  /**
   * @notice Unpacked data of an auction
   * @param  _id Id of the auction
   * @return _bidAmount How much protocol tokens are to be minted [wad]
   * @return _amountToSell How many system coins are raised [rad]
   * @return _highBidder Address of the highest bidder
   * @return _bidExpiry Time when the latest bid expires and the auction can be settled
   * @return _auctionDeadline Time when the auction expires
   */
  // solhint-disable-next-line private-vars-leading-underscore
  function _auctions(uint256 _id)
    external
    view
    returns (
      uint256 _bidAmount,
      uint256 _amountToSell,
      address _highBidder,
      uint256 _bidExpiry,
      uint256 _auctionDeadline
    );

  /// @notice Total amount of debt auctions created
  function auctionsStarted() external view returns (uint256 _auctionsStarted);

  /// @notice Total amount of simultaneous active debt auctions
  function activeDebtAuctions() external view returns (uint256 _activeDebtAuctions);

  // --- Registry ---

  /// @notice Address of the SAFEEngine contract
  function safeEngine() external view returns (ISAFEEngine _safeEngine);
  /// @notice Address of the ProtocolToken contract
  function protocolToken() external view returns (IProtocolToken _protocolToken);
  /// @notice Address of the AccountingEngine contract
  function accountingEngine() external view returns (address _accountingEngine);

  // --- Params ---

  /**
   * @notice Getter for the contract parameters struct
   * @return _dahParams Auction house parameters struct
   */
  function params() external view returns (DebtAuctionHouseParams memory _dahParams);

  /**
   * @notice Getter for the unpacked contract parameters struct
   * @return _bidDecrease Minimum bid increase compared to the last bid in order to take the new one in consideration [wad %]
   * @return _amountSoldIncrease Increase in protocol tokens sold in case an auction is restarted [wad %]
   * @return _bidDuration How long the auction lasts after a new bid is submitted [seconds]
   * @return _totalAuctionLength Total length of the auction [seconds]
   */
  // solhint-disable-next-line private-vars-leading-underscore
  function _params()
    external
    view
    returns (uint256 _bidDecrease, uint256 _amountSoldIncrease, uint256 _bidDuration, uint256 _totalAuctionLength);

  // --- Auction ---

  /**
   * @notice Start a new debt auction
   * @param  _incomeReceiver Who receives the auction proceeds
   * @param  _amountToSell Initial amount of protocol tokens to be minted [wad]
   * @param  _initialBid Amount of debt to be sold [rad]
   * @return _id Id of the auction
   */
  function startAuction(
    address _incomeReceiver,
    uint256 _amountToSell,
    uint256 _initialBid
  ) external returns (uint256 _id);

  /**
   * @notice Restart an auction if no bids were placed
   * @dev    An auction can be restarted if the auction expired with no bids
   * @param  _id Id of the auction
   */
  function restartAuction(uint256 _id) external;

  /**
   * @notice Decrease the protocol token amount you're willing to receive in
   *         exchange for providing the same amount of system coins being raised by the auction
   * @param  _id ID of the auction for which you want to submit a new bid
   * @param  _amountToBuy Amount of protocol tokens to buy (must be smaller than the previous proposed amount) [wad]
   */
  function decreaseSoldAmount(uint256 _id, uint256 _amountToBuy) external;

  /**
   * @notice Settle an auction
   * @dev    Can only be called after the auction expired with a winning bid
   * @param  _id Id of the auction
   */
  function settleAuction(uint256 _id) external;

  /**
   * @notice Terminate an auction prematurely
   * @param  _id Id of the auction
   * @dev    Can only be called after the contract is disabled
   * @dev    The method creates an unbacked debt position in the AccountingEngine for the remaining debt
   */
  function terminateAuctionPrematurely(uint256 _id) external;
}

// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.20;

import {ISAFEEngine} from '@interfaces/ISAFEEngine.sol';
import {IProtocolToken} from '@interfaces/tokens/IProtocolToken.sol';

interface ICommonSurplusAuctionHouse {
  // --- Events ---

  /**
   * @notice Emitted when a new auction is started
   * @param  _id Id of the auction
   * @param  _auctioneer Address who started the auction
   * @param  _blockTimestamp Time when the auction was started
   * @param  _amountToSell How many protocol tokens are initially bidded [wad]
   * @param  _amountToRaise Amount of system coins to raise [rad]
   * @param  _auctionDeadline Time when the auction expires
   */
  event StartAuction(
    uint256 indexed _id,
    address indexed _auctioneer,
    uint256 _blockTimestamp,
    uint256 _amountToSell,
    uint256 _amountToRaise,
    uint256 _auctionDeadline
  );

  /**
   * @notice Emitted when an auction is restarted
   * @param  _id Id of the auction
   * @param  _blockTimestamp Time when the auction was restarted
   * @param  _auctionDeadline New time when the auction expires
   */
  event RestartAuction(uint256 indexed _id, uint256 _blockTimestamp, uint256 _auctionDeadline);

  /**
   * @notice Emitted when a bid is made in an auction
   * @param  _id Id of the auction
   * @param  _bidder Who made the bid
   * @param  _blockTimestamp Time when the bid was made
   * @param  _raisedAmount Amount of system coins raised in the bid [rad]
   * @param  _soldAmount Amount of protocol tokens offered to buy in the bid [wad]
   * @param  _bidExpiry Time when the bid expires
   */
  event IncreaseBidSize(
    uint256 indexed _id,
    address _bidder,
    uint256 _blockTimestamp,
    uint256 _raisedAmount,
    uint256 _soldAmount,
    uint256 _bidExpiry
  );

  /**
   * @notice Emitted when an auction is settled
   * @param  _id Id of the auction
   * @param  _blockTimestamp Time when the auction was settled
   * @param  _highBidder Who won the auction
   * @param  _raisedAmount Amount of system coins raised in the auction [rad]
   */
  event SettleAuction(uint256 indexed _id, uint256 _blockTimestamp, address _highBidder, uint256 _raisedAmount);

  // --- Errors ---

  /// @dev Throws when trying to bid in an auction that hasn't started yet
  error SAH_AuctionNeverStarted();
  /// @dev Throws when trying to settle an auction that hasn't finished yet
  error SAH_AuctionNotFinished();
  /// @dev Throws when trying to bid in an auction that has already expired
  error SAH_AuctionAlreadyExpired();
  /// @dev Throws when trying to bid in an auction that has an expired bid
  error SAH_BidAlreadyExpired();
  /// @dev Throws when trying to restart an auction that has an active bid
  error SAH_BidAlreadyPlaced();
  /// @dev Throws when trying to place a bid that differs from the amount to raise
  error SAH_AmountsNotMatching();
  /// @dev Throws when trying to place a bid that is not higher than the previous one
  error SAH_BidNotHigher();
  /// @dev Throws when trying to place a bid that is not higher than the previous one by the minimum increase
  error SAH_InsufficientIncrease();
  /// @dev Throws when trying to prematurely terminate an auction that has no bids
  error SAH_HighBidderNotSet();

  // --- Data ---

  struct Auction {
    // Bid size (how many protocol tokens are offered per system coins sold)
    uint256 /* WAD  */ bidAmount;
    // How many system coins are sold in an auction
    uint256 /* RAD  */ amountToSell;
    // Who the high bidder is
    address /*      */ highBidder;
    // When the latest bid expires and the auction can be settled
    uint256 /* unix */ bidExpiry;
    // Hard deadline for the auction after which no more bids can be placed
    uint256 /* unix */ auctionDeadline;
  }

  /**
   * @notice Type of the auction house
   * @return _auctionHouseType Bytes32 representation of the auction house type
   */
  // solhint-disable-next-line func-name-mixedcase
  function AUCTION_HOUSE_TYPE() external view returns (bytes32 _auctionHouseType);

  /**
   * @notice Data of an auction
   * @param  _id Id of the auction
   * @return _auction Auction data struct
   */
  function auctions(uint256 _id) external view returns (Auction memory _auction);

  /**
   * @notice Raw data of an auction
   * @param  _id Id of the auction
   * @return _bidAmount How many system coins are offered for the protocol tokens [rad]
   * @return _amountToSell How protocol tokens are sold to buy the surplus system coins [wad]
   * @return _highBidder Who the high bidder is
   * @return _bidExpiry When the latest bid expires and the auction can be settled [timestamp]
   * @return _auctionDeadline Hard deadline for the auction after which no more bids can be placed [timestamp]
   */
  // solhint-disable-next-line private-vars-leading-underscore
  function _auctions(uint256 _id)
    external
    view
    returns (
      uint256 _bidAmount,
      uint256 _amountToSell,
      address _highBidder,
      uint256 _bidExpiry,
      uint256 _auctionDeadline
    );

  /// @notice Total amount of surplus auctions created
  function auctionsStarted() external view returns (uint256 _auctionsStarted);

  // --- Registry ---

  /// @notice Address of the SAFEEngine contract
  function safeEngine() external view returns (ISAFEEngine _safeEngine);

  /// @notice Address of the ProtocolToken contract
  function protocolToken() external view returns (IProtocolToken _protocolToken);

  // --- Auction ---

  /**
   * @notice Start a new surplus auction
   * @param  _amountToSell Total amount of system coins to sell [rad]
   * @param  _initialBid Initial protocol token bid [wad]
   * @return _id ID of the started auction
   */
  function startAuction(uint256 _amountToSell, uint256 _initialBid) external returns (uint256 _id);

  /**
   * @notice Restart an auction if no bids were submitted for it
   * @param  _id ID of the auction to restart
   */
  function restartAuction(uint256 _id) external;

  /**
   * @notice Submit a higher protocol token bid for the same amount of system coins
   * @param  _id ID of the auction you want to submit the bid for
   * @param  _bid New bid submitted [wad]
   */
  function increaseBidSize(uint256 _id, uint256 _bid) external;

  /**
   * @notice Settle/finish an auction
   * @param  _id ID of the auction to settle
   */
  function settleAuction(uint256 _id) external;
}

// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.20;

import {IERC20Metadata} from '@openzeppelin/contracts/token/ERC20/extensions/IERC20Metadata.sol';
import {IERC20Permit} from '@openzeppelin/contracts/token/ERC20/extensions/IERC20Permit.sol';
import {IVotes} from '@openzeppelin/contracts/governance/utils/IVotes.sol';

import {IAuthorizable} from '@interfaces/utils/IAuthorizable.sol';

interface IProtocolToken is IERC20Metadata, IERC20Permit, IVotes, IAuthorizable {
  // --- Methods ---

  /**
   * @notice Mint an amount of tokens to an account
   * @param _account Address of the account to mint tokens to
   * @param _amount Amount of tokens to mint [wad]
   * @dev   Only authorized addresses can mint tokens
   */
  function mint(address _account, uint256 _amount) external;

  /**
   * @notice Burn an amount of tokens from the sender
   * @param _amount Amount of tokens to burn [wad]
   */
  function burn(uint256 _amount) external;

  /**
   * @notice Unpause the token transfers, minting and burning
   * @dev    Only authorized addresses can unpause the token
   */
  function unpause() external;
}

// SPDX-License-Identifier: MIT
// OpenZeppelin Contracts (last updated v5.0.0) (token/ERC20/extensions/IERC20Metadata.sol)

pragma solidity ^0.8.20;

import {IERC20} from "../IERC20.sol";

/**
 * @dev Interface for the optional metadata functions from the ERC20 standard.
 */
interface IERC20Metadata is IERC20 {
    /**
     * @dev Returns the name of the token.
     */
    function name() external view returns (string memory);

    /**
     * @dev Returns the symbol of the token.
     */
    function symbol() external view returns (string memory);

    /**
     * @dev Returns the decimals places of the token.
     */
    function decimals() external view returns (uint8);
}

// SPDX-License-Identifier: MIT
// OpenZeppelin Contracts (last updated v5.0.0) (token/ERC20/extensions/IERC20Permit.sol)

pragma solidity ^0.8.20;

/**
 * @dev Interface of the ERC20 Permit extension allowing approvals to be made via signatures, as defined in
 * https://eips.ethereum.org/EIPS/eip-2612[EIP-2612].
 *
 * Adds the {permit} method, which can be used to change an account's ERC20 allowance (see {IERC20-allowance}) by
 * presenting a message signed by the account. By not relying on {IERC20-approve}, the token holder account doesn't
 * need to send a transaction, and thus is not required to hold Ether at all.
 *
 * ==== Security Considerations
 *
 * There are two important considerations concerning the use of `permit`. The first is that a valid permit signature
 * expresses an allowance, and it should not be assumed to convey additional meaning. In particular, it should not be
 * considered as an intention to spend the allowance in any specific way. The second is that because permits have
 * built-in replay protection and can be submitted by anyone, they can be frontrun. A protocol that uses permits should
 * take this into consideration and allow a `permit` call to fail. Combining these two aspects, a pattern that may be
 * generally recommended is:
 *
 * ```solidity
 * function doThingWithPermit(..., uint256 value, uint256 deadline, uint8 v, bytes32 r, bytes32 s) public {
 *     try token.permit(msg.sender, address(this), value, deadline, v, r, s) {} catch {}
 *     doThing(..., value);
 * }
 *
 * function doThing(..., uint256 value) public {
 *     token.safeTransferFrom(msg.sender, address(this), value);
 *     ...
 * }
 * ```
 *
 * Observe that: 1) `msg.sender` is used as the owner, leaving no ambiguity as to the signer intent, and 2) the use of
 * `try/catch` allows the permit to fail and makes the code tolerant to frontrunning. (See also
 * {SafeERC20-safeTransferFrom}).
 *
 * Additionally, note that smart contract wallets (such as Argent or Safe) are not able to produce permit signatures, so
 * contracts should have entry points that don't rely on permit.
 */
interface IERC20Permit {
    /**
     * @dev Sets `value` as the allowance of `spender` over ``owner``'s tokens,
     * given ``owner``'s signed approval.
     *
     * IMPORTANT: The same issues {IERC20-approve} has related to transaction
     * ordering also apply here.
     *
     * Emits an {Approval} event.
     *
     * Requirements:
     *
     * - `spender` cannot be the zero address.
     * - `deadline` must be a timestamp in the future.
     * - `v`, `r` and `s` must be a valid `secp256k1` signature from `owner`
     * over the EIP712-formatted function arguments.
     * - the signature must use ``owner``'s current nonce (see {nonces}).
     *
     * For more information on the signature format, see the
     * https://eips.ethereum.org/EIPS/eip-2612#specification[relevant EIP
     * section].
     *
     * CAUTION: See Security Considerations above.
     */
    function permit(
        address owner,
        address spender,
        uint256 value,
        uint256 deadline,
        uint8 v,
        bytes32 r,
        bytes32 s
    ) external;

    /**
     * @dev Returns the current nonce for `owner`. This value must be
     * included whenever a signature is generated for {permit}.
     *
     * Every successful call to {permit} increases ``owner``'s nonce by one. This
     * prevents a signature from being used multiple times.
     */
    function nonces(address owner) external view returns (uint256);

    /**
     * @dev Returns the domain separator used in the encoding of the signature for {permit}, as defined by {EIP712}.
     */
    // solhint-disable-next-line func-name-mixedcase
    function DOMAIN_SEPARATOR() external view returns (bytes32);
}

// SPDX-License-Identifier: MIT
// OpenZeppelin Contracts (last updated v5.0.0) (governance/utils/IVotes.sol)
pragma solidity ^0.8.20;

/**
 * @dev Common interface for {ERC20Votes}, {ERC721Votes}, and other {Votes}-enabled contracts.
 */
interface IVotes {
    /**
     * @dev The signature used has expired.
     */
    error VotesExpiredSignature(uint256 expiry);

    /**
     * @dev Emitted when an account changes their delegate.
     */
    event DelegateChanged(address indexed delegator, address indexed fromDelegate, address indexed toDelegate);

    /**
     * @dev Emitted when a token transfer or delegate change results in changes to a delegate's number of voting units.
     */
    event DelegateVotesChanged(address indexed delegate, uint256 previousVotes, uint256 newVotes);

    /**
     * @dev Returns the current amount of votes that `account` has.
     */
    function getVotes(address account) external view returns (uint256);

    /**
     * @dev Returns the amount of votes that `account` had at a specific moment in the past. If the `clock()` is
     * configured to use block numbers, this will return the value at the end of the corresponding block.
     */
    function getPastVotes(address account, uint256 timepoint) external view returns (uint256);

    /**
     * @dev Returns the total supply of votes available at a specific moment in the past. If the `clock()` is
     * configured to use block numbers, this will return the value at the end of the corresponding block.
     *
     * NOTE: This value is the sum of all available votes, which is not necessarily the sum of all delegated votes.
     * Votes that have not been delegated are still part of total supply, even though they would not participate in a
     * vote.
     */
    function getPastTotalSupply(uint256 timepoint) external view returns (uint256);

    /**
     * @dev Returns the delegate that `account` has chosen.
     */
    function delegates(address account) external view returns (address);

    /**
     * @dev Delegates votes from the sender to `delegatee`.
     */
    function delegate(address delegatee) external;

    /**
     * @dev Delegates votes from signer to `delegatee`.
     */
    function delegateBySig(address delegatee, uint256 nonce, uint256 expiry, uint8 v, bytes32 r, bytes32 s) external;
}

// SPDX-License-Identifier: MIT
// OpenZeppelin Contracts (last updated v5.0.0) (token/ERC20/IERC20.sol)

pragma solidity ^0.8.20;

/**
 * @dev Interface of the ERC20 standard as defined in the EIP.
 */
interface IERC20 {
    /**
     * @dev Emitted when `value` tokens are moved from one account (`from`) to
     * another (`to`).
     *
     * Note that `value` may be zero.
     */
    event Transfer(address indexed from, address indexed to, uint256 value);

    /**
     * @dev Emitted when the allowance of a `spender` for an `owner` is set by
     * a call to {approve}. `value` is the new allowance.
     */
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Returns the value of tokens in existence.
     */
    function totalSupply() external view returns (uint256);

    /**
     * @dev Returns the value of tokens owned by `account`.
     */
    function balanceOf(address account) external view returns (uint256);

    /**
     * @dev Moves a `value` amount of tokens from the caller's account to `to`.
     *
     * Returns a boolean value indicating whether the operation succeeded.
     *
     * Emits a {Transfer} event.
     */
    function transfer(address to, uint256 value) external returns (bool);

    /**
     * @dev Returns the remaining number of tokens that `spender` will be
     * allowed to spend on behalf of `owner` through {transferFrom}. This is
     * zero by default.
     *
     * This value changes when {approve} or {transferFrom} are called.
     */
    function allowance(address owner, address spender) external view returns (uint256);

    /**
     * @dev Sets a `value` amount of tokens as the allowance of `spender` over the
     * caller's tokens.
     *
     * Returns a boolean value indicating whether the operation succeeded.
     *
     * IMPORTANT: Beware that changing an allowance with this method brings the risk
     * that someone may use both the old and the new allowance by unfortunate
     * transaction ordering. One possible solution to mitigate this race
     * condition is to first reduce the spender's allowance to 0 and set the
     * desired value afterwards:
     * https://github.com/ethereum/EIPs/issues/20#issuecomment-263524729
     *
     * Emits an {Approval} event.
     */
    function approve(address spender, uint256 value) external returns (bool);

    /**
     * @dev Moves a `value` amount of tokens from `from` to `to` using the
     * allowance mechanism. `value` is then deducted from the caller's
     * allowance.
     *
     * Returns a boolean value indicating whether the operation succeeded.
     *
     * Emits a {Transfer} event.
     */
    function transferFrom(address from, address to, uint256 value) external returns (bool);
}
