from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
  # Overview - For each number that comes up, check if going forward
  # is closer, or going backwards is closer. The main thing to realize
  # is that because the lock is circular, a number on the lock, x, is
  # equivalent to that number plus any number of rotations, such as
  # x-2N, x-N, x, x+N, x+2N, etc. So if the number you want to go to is
  # bigger, you can check if it's shorter to go right from x, or left
  # from x+N. If the number you want to go to is smaller, you can check
  # if it's shorter to go left to it, or go right to target+N. Note
  # that going left to a number is the same (time or steps) as coming
  # from it on the right. So the operation is the same in both cases,
  # but you may have to switch the numbers to be going from a lower
  # number to a higher number.
  total_time = 0
  # Starting at 1.
  curr_pos = 1 
  for c in C:
    # Don't need to do anything if the target is already where we are.
    if curr_pos == c:
      continue
    # Find and set the smaller and larger of the current position and
    # the target.
    if curr_pos < c:
      smaller = curr_pos
      larger = c
    else:
      smaller = c
      larger = curr_pos
    # Distance going right from smaller to larger.
    right_dist = larger - smaller
    # Distance going left from smaller+N to larger.
    left_dist = smaller + N - larger
    # Add the smaller time.
    total_time += min(right_dist, left_dist)
    # Set the new current position.
    curr_pos = c
  return total_time
