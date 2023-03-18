from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
  
  # Recursion is interesting, but it runs too slowly.
  
  return getMinCodeEntryTimeHelper(N, M, C, 1, 1, 0)

def getMinCodeEntryTimeHelper(N: int, M: int, C: List[int], left_pos: int, right_pos: int, total: int) -> int:
  if M == 0:
    return total
  # If the locks are on the same number, then only need to move one.
  if left_pos == right_pos:
    rotate_time = getMinSingleRotateTime(N, left_pos, C[0])
    return getMinCodeEntryTimeHelper(N, M-1, C[1:], C[0], right_pos, total + rotate_time)
  # Else, find the totals of what you would get if you moved either the left or the right
  # lock and use the smaller one.
  else:
    left_time = getMinSingleRotateTime(N, left_pos, C[0])
    total_left_time = getMinCodeEntryTimeHelper(N, M-1, C[1:], C[0], right_pos, total + left_time)
    right_time = getMinSingleRotateTime(N, right_pos, C[0])
    total_right_time = getMinCodeEntryTimeHelper(N, M-1, C[1:], left_pos, C[0], total + right_time)
    return min(total_left_time, total_right_time)

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
