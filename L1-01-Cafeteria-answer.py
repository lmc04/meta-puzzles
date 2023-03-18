from typing import List
# Write any import statements here
import math

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  # If there are no diners sitting, then we can directly say how many will fit at the table.
  if M == 0:
    return getMaxAdditionalDinersCountEmptyTable(N, K)
  # Sort the sitting seat positions but do not change the input version.
  sorted_seats = list(S)
  sorted_seats.sort()
  # Take care of any spots from the start of the table to the first diner.
  spots_avail = sorted_seats[0] - 1 - K
  total = getMaxAdditionalDinersCountEmptyTable(spots_avail, K)
  # Take care of any spots in between diners.
  # Start from the second diner so there will always be one before.
  for i in range(1,M):
    # The two seat positions minus one are the seats in between the diners
    # and take away another 2*K for the empty spaces on one side of both diners.
    spots_avail = sorted_seats[i] - sorted_seats[i-1] - 1 - 2*K
    total += getMaxAdditionalDinersCountEmptyTable(spots_avail, K)
  # Take care of any spots from the last diner to the end of the table.
  spots_avail = N - sorted_seats[-1] - K
  total += getMaxAdditionalDinersCountEmptyTable(spots_avail, K)
  return total

def getMaxAdditionalDinersCountEmptyTable(N: int, K: int) -> int:
  # If there are no diners sitting, then we can directly say how many will fit at the table.
  # No spots means no diners.
  if N < 1:
    return 0
  # If people can sit every J-th seat, then the number of people that can fit are
  # how many times J goes into N plus 1 more if there is a fractional fit because
  # a person can be seated at the first of those number of seats < J at the end.
  fractional_fits = N/(K+1)
  return math.ceil(fractional_fits)

# Rough
#1 2 3 4 5 6 7 8 9 10  - 10/1  = 10
#1 3 5 7 9 - 10/2 = 5
#1 4 7 10 - 10/3 = 3.3333 -> 4
#1 5 9 - 10/4 = 2.5 -> 3
#1 6 - 10/5 = 2
#1 7 - 10/6 = 1.66666 -> 2
#1 8 - 10/7 = 1.xx -> 2 
#1 9 - 10/8 = 1.25 -> 2
#1 10 - 10/9 = 1.1111 -> 2
#1 - 10/10 = 1
#10/(10+x) = 0.xx -> 1
#
#1 2 3 4 5 6 7 8 9 - 9/1 = 9
#1 3 5 7 9 - 9/2 = 4.5 -> 5
#1 4 7 - 9/3 = 3
#1 5 9 - 9/4 = 2.25 -> 3
#1 6 - 9/5 = 1.8 -> 2
#1 7 - 9/6 = 1.3333 -> 2
#1 8 - 9/7 = 1.xx -> 2
#1 9 - 9/8 = 1.125 -> 2
#1 - 9/9 = 1
