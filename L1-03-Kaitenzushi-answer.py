from typing import List
# Write any import statements here
import queue

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # Write your code here
  # Keep track of the last dishes eaten in a Queue and also with a dictionary
  # that tells whether you can eat a dish or not. When the Queue is full and
  # a new type of dish is eaten, get the oldest dish from the queue and make
  # it eatable again. Count up the eaten dishes.
  q = queue.Queue()
  can_eat = {}
  total_eaten = 0
  for i in range(N):
    # See if we can eat the dish.
    # If it is not yet in the dict, it will return True instead of an error.
    if can_eat.get(D[i], True):
      total_eaten += 1
      # If we have already eaten K different dishes, then the oldest can be
      # eaten again.
      if q.qsize() == K:
        # Get the oldest and make it eatable again.
        oldest_eaten = q.get()
        can_eat[oldest_eaten] = True
      # Add the new dish to the queue and make it not eatable.
      q.put(D[i])
      can_eat[D[i]] = False
  return total_eaten
