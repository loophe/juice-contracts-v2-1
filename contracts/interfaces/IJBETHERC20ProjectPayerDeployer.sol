// SPDX-License-Identifier: MIT
pragma solidity 0.8.6;

import './IJBDirectory.sol';
import './IJBProjectPayer.sol';

interface IJBETHERC20ProjectPayerDeployer {
  event DeployProjectPayer(
    IJBProjectPayer indexed projectPayer,
    uint256 indexed defaultProjectId,
    address indexed defaultBeneficiary,
    bool defaultPreferClaimedTokens,
    string defaultMemo,
    bytes defaultMetadata,
    IJBDirectory directory,
    address owner,
    address caller
  );

  function deployProjectPayer(
    uint256 _defaultProjectId,
    address payable _defaultBeneficiary,
    bool _defaultPreferClaimedTokens,
    string memory _defaultMemo,
    bytes memory _defaultMetadata,
    IJBDirectory _directory,
    address _owner
  ) external returns (IJBProjectPayer projectPayer);
}
