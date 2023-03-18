# Write any import statements here

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
  
  # This takes too long to run in the time limit.
  
  # Overview - Go through the cells looking for the starting letter of a
  # photograph. If we find it, look X to Y positions away on both sides for
  # an A. For all the As found there, look outwards X to Y positions again
  # for the ending letter of a photograph. If there are, then those are artistic.
  #P_count = C.count('P')
  #B_count = C.count('B')
  #if P_count < B_count:
  #  starting_letter = 'P'
  #  ending_letter = 'B'
  #else:
  #  starting_letter = 'B'
  #  ending_letter = 'P'
  C = C.strip('.A')
  starting_letter = 'P'
  ending_letter = 'B'
  artistic_total = 0
  for i in range(len(C)):
    if C[i] == starting_letter:
      # Check left.
      # Get the indices where where expecting As.
      # Negative indices look from the end of the string and we don't want that.
      start_slice = max(0, i - Y)
      # +1 on the right end to cover the correct index.
      end_slice = max(0, i - X + 1)
      A_ind = C.find('A', start_slice, end_slice)
      # The index is -1 if there is no A in the slice.
      while A_ind != -1:
        # Get the slice indeces where expecting the photograph ending letter.
        start_count = max(0, A_ind - Y)
        end_count = max(0, A_ind - X + 1)
        # The number of ending letters here represents the possible artistic photographs.
        artistic_total += C.count(ending_letter, start_count, end_count)
        # Find the next occurence of A to check the next set of photographs.
        A_ind = C.find('A', A_ind + 1, end_slice)
      # Check right.
      # Slice indices can be greater than the end of the string with no issue.
      start_slice = i + X
      end_slice = i + Y + 1
      A_ind = C.find('A', start_slice, end_slice)
      while A_ind != -1:
        start_count = A_ind + X
        end_count = A_ind + Y + 1
        artistic_total += C.count(ending_letter, start_count, end_count)
        A_ind = C.find('A', A_ind + 1, end_slice)
  return artistic_total
