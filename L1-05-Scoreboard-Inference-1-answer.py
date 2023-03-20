from typing import List
# Write any import statements here
import numpy as np

def getMinProblemCount(N: int, S: List[int]) -> int:
  # Write your code here
  # Since we want the lowest number of questions, we want to use as many
  # of the highest value problems possible. This means using as many 2-value
  # problems as possible. If we only use 2-value problems, then we could
  # cover all of the even scores. To cover the odd scores, we just need to
  # add one 1-value problem (use 2-value problems to go to the nearest even
  # value less than the odd score, then add the 1-value problem.)
  # This means if we have M 2-value problems, we can cover all even scores
  # up to 2M -> {2m | for all m in 0 to M}.
  # If we have M 2-value problems and 1 1-value problem, we can cover all
  # scores up to 2M+1 -> {2m, 2m+1 | for all m in 0 to M}.
  # As seen in Sample test case #2, if the max score is even but there are
  # odd scores, too, it does not fit into the above 2 cases. We would need
  # at least 1 1-value problem to cover the odd score(s). We can either
  # use M = max_score/2 2-value problems and 1 1-value problem (total M+1)
  # or replace a 2-value problem with 2 1-value problems (total M-1 + 2 =
  # M+1). Either way is the same total.
  # This covers all cases.
  #
  # The max score is the important one.
  max_score = max(S)
  # First check if all the scores are even because then we just need half
  # the max score in 2-value problems.
  # Turn S into an array to evaluate all elements at once.
  S_array = np.array(S)
  # Use mod to see if the elements are even or odd.
  remainders = S_array % 2
  # If all remainders are 0, then all scores were even.
  if np.all(remainders == 0):
      # Need only 2-value problems.
      return max_score // 2
  # There is an odd score and the max is odd, too.
  elif max_score % 2 == 1:
      # Need 2-value problems up to the even number below the max, then
      # 1 1-value problem.
      return (max_score - 1) // 2 + 1
  # There is an odd score but the max is even.
  else:
      # Need 2-value problems up to the max, and 1 1-value problem
      # to cover all the odd numbers below it.
      return max_score // 2 + 1
