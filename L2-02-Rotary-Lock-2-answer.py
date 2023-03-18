from typing import List, Tuple
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
  # Can't do recursion, so instead keep track of the "leaf" totals
  # at each step and if there are two of the same leaves at the same
  # step, just keep the faster one.
  # Initialize it to one after the starting position because it does
  # not matter which lock you select first. Also M is at least 1 so
  # no index issues.
  leaves = {(C[0], 1): getMinSingleRotateTime(N, 1, C[0])}
  for c in C:
    # Need a new dict because we need to compare the leaves
    # on the lower level, not with the existing ones that
    # will be shorter, but does not represent the current
    # rotation.
    child_leaves = {}
    # Go through the existing leaves and see what happens if you
    # rotate the left or the right lock.
    for pos in leaves:
      # The times for the current step of adding rotating the left
      # and right locks.
      left_time = leaves[pos] + getMinSingleRotateTime(N, pos[0], c)
      right_time = leaves[pos] + getMinSingleRotateTime(N, pos[1], c)
      # Keep track of the times, but only if they're better.
      addLeafIfLessTime(child_leaves, (c, pos[1]), left_time)
      addLeafIfLessTime(child_leaves, (pos[0], c), right_time)
    # The new child leaves will be the base nodes of the next step.
    leaves = child_leaves
  # The best time is just the min of all the times at the last step.
  return min(leaves.values())

def getMinSingleRotateTime(N:int, curr_pos: int, target: int) -> int:
  # Don't need to do anything if the target is already where we are.
  if curr_pos == target:
    return 0
  # Find and set the smaller and larger of the current position and
  # the target.
  if curr_pos < target:
    smaller = curr_pos
    larger = target
  else:
    smaller = target
    larger = curr_pos
  # Distance going right from smaller to larger.
  right_dist = larger - smaller
  # Distance going left from smaller+N to larger.
  left_dist = smaller + N - larger
  # Select the smaller time.
  return min(right_dist, left_dist)

def addLeafIfLessTime(leaves: dict, pos: Tuple[int, int], time: int) -> None:
  # Add the position and time if not present or update it with the
  # best (lowest) time if it is.
  if (pos not in leaves) or (time < leaves[pos]):
    leaves[pos] = time
