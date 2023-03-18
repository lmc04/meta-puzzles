# Write any import statements here

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
  
  # This takes too long to run in the time limit.
  
  # Overview - Go through the cells looking for A, the middle of a photograph.
  # If we find it, look to the left and right X to Y positions away for the start
  # and end of a photograph (P/B). The Ps on one side times the Bs on the other is
  # the number of artistic photographs.
  artistic_total = 0
  # Strip leading and trailing '.' and 'A' since photographs cannot start or end
  # with them.
  C = C.strip('.A')
  for i in range(len(C)):
    if C[i] == 'A':
      # Get slice indices of where to look for start and ends of photographs.
      # Negative indices look from the end of the string and we don't want that.
      left_start = max(0, i - Y)
      # +1 on the right end to cover the correct index.
      left_end = max(0, i - X + 1)
      # Slice indices can be greater than the end of the string with no issue.
      right_start = i + X
      right_end = i + Y + 1
      # Count the Ps and Bs in the slices.
      left_Ps = C.count('P', left_start, left_end)
      left_Bs = C.count('B', left_start, left_end)
      right_Ps = C.count('P', right_start, right_end)
      right_Bs = C.count('B', right_start, right_end)
      # Add the possible artistic photographs.
      artistic_total += left_Ps * right_Bs + left_Bs * right_Ps
  return artistic_total
