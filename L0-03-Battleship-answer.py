from typing import List
# Write any import statements here
import numpy as np

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  # Write your code here
  # Turn the List into an array so it can be summed over all axes.
  G_array = np.array(G,dtype=int)
  # Get the number of cells that have a ship.
  occupied_num = np.sum(G_array)
  # Chance of hitting is cells that have a ship over all cells.
  # Not converting ints to floats because python takes care of that now.
  return occupied_num/(R*C)
