# Write any import statements here

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
  # Notes - Takes too long making all photos possible first.
  #       - Takes too long looking for P then checking windows for A then B.
  #       - Takes too long looking for A and counting Ps and Bs in windows.
  # Overview - Go through all the cells keeping track of P and B counts in windows.
  # Each step update window counts only needing to look at the start and ends of
  # windows. If cell is A, use already counted Ps and Bs in windows. The Ps on one
  # side times the Bs on the other is the number of artistic photographs.
  artistic_total = 0
  # Strip leading and trailing '.' and 'A' since photographs cannot start or end
  # with them.
  C = C.strip('.A')
  N = len(C)
  left_Ps = 0
  left_Bs = 0
  # Count to the right as if we are one spot to the left of the start of the string.
  # Slice indices can be greater than the end of the string with no issue.
  # +1 on the right end to cover the correct index.
  right_Ps = C.count('P', -1 + X, -1 + Y + 1)
  right_Bs = C.count('B', -1 + X, -1 + Y + 1)
  for i in range(N):
    # Get the indices of the start and ends of the left and right windows.
    # Each step, only the charactes at the ends of the windows will change,
    # while everything inside the windows will be the same so the total
    # count is only affected by the character that drops out and the
    # character that enters.
    # An extra -1 is needed for the drop indices because it is one spot to
    # left of the window.
    left_drop = i - Y - 1
    left_enter = i - X
    right_drop = i + X - 1
    right_enter = i + Y
    # If the indices are inside the string, check if P or B and subtract one
    # on drops or add one on enters.
    if left_drop >= 0:
      if C[left_drop] == 'P':
        left_Ps -= 1
      elif C[left_drop] == 'B':
        left_Bs -= 1
    if left_enter >= 0:
      if C[left_enter] == 'P':
        left_Ps += 1
      elif C[left_enter] == 'B':
        left_Bs += 1
    if right_drop < N:
      if C[right_drop] == 'P':
        right_Ps -= 1
      elif C[right_drop] == 'B':
        right_Bs -= 1
    if right_enter < N:
      if C[right_enter] == 'P':
        right_Ps += 1
      elif C[right_enter] == 'B':
        right_Bs += 1
    # On As, use the left and right counts to get the number of artistic photographs.
    if C[i] == 'A':
      # Add the possible artistic photographs.
      artistic_total += left_Ps * right_Bs + left_Bs * right_Ps
  return artistic_total
