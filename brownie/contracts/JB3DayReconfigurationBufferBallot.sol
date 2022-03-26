// SPDX-License-Identifier: MIT
pragma solidity 0.8.6;

import './interfaces/IJBFundingCycleBallot.sol';

/** 
   @notice Manages approving funding cycle reconfigurations automatically after a buffer period of 3 days.
 */
contract JB3DayReconfigurationBufferBallot is IJBFundingCycleBallot {
  // --- public stored properties --- //

  /// @notice The number of seconds that must pass for a funding cycle reconfiguration to become active.
  uint256 public constant DELAY = 259200; // 3 days

  // --- external views --- //

  /** 
    @notice 
    The time that this ballot is active for.

    @dev A ballot should not be considered final until the duration has passed.

    @return The duration in seconds.
  */
  function duration() external pure override returns (uint256) {
    return DELAY;
  }

  /**
      @notice 
      The approval state of a particular funding cycle.

      @param _configured The configuration of the funding cycle to check the state of.

      @return The state of the provided ballot.
   */
  function stateOf(uint256, uint256 _configured) external view override returns (JBBallotState) {
    return block.timestamp > _configured + DELAY ? JBBallotState.Approved : JBBallotState.Active;
  }
}
