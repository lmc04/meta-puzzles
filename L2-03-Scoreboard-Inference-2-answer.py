from typing import List
# Write any import statements here
import numpy as np

def getMinProblemCount(N: int, S: List[int]) -> int:
  # Write your code here
  # The idea for this one is very similar to the Chapter 1 version of this
  # puzzle. We want to try to get as many 3-value problems in, substituting
  # or adding 1- or 2-value problems as needed. And it is mostly determined
  # by the max score and the divisibility of the scores by 3.
  # If the scores are all divisible by 3, then they can all be covered up to
  # 3M -> {3m | for all m in 0 to M}. If there is a score (or scores) that
  # is not the max that is not divisible by 3 (remainder 1, remainder 2, or 
  # both), all these cases can be taken care of by swapping a 3-value
  # problem with a 1- and a 2- value problem. So for M-1 + 2 = M+1 problems
  # we can cover up to the same max score but also the non-multiples of 3
  # -> {3m, 3m+1, 3m+2, 3m+1+2 | for all m in 0 to M-1}.
  # If the max score is a remainder 2, then the only way to get to it is by
  # going up to the closest lowest multiple of 3 with 3-value problems and
  # adding 1 2-value problem. This will also cover all remainder 2 scores
  # that are smaller -> {3m, 3m+2 | for all m in 0 to M}. If there are also
  # remainder 1 scores that are not the max, then we just have to add 1
  # 1-value problem -> {3m, 3m+1, 3m+2 | for all m in 0 to M}.
  # If the max score is a remainder 1, then it's the same idea but with 1-
  # and 2-value problem additions switched so the number of problems are
  # the same.
  # BUT there is one case where you can eliminate an unnecessary
  # 3-value problem. If the max score is a remainder 1, and the 2nd max
  # score is 2 less (remainder 2) (ex. [2, 4] or [5, 7]), then the steps
  # above would say to use 3-value problems to cover up to max-1 scores,
  # then add a 1-value problem to hit the max score, and also a 2-value
  # problem to hit the 2nd max. But that last 3-value problem is hitting
  # a multiple of 3 score that doesn't exist in the score list and instead
  # the max can be reached by going with 3-value problems up to the max-4
  # score, then 2 2-value problems to hit the 2nd max and max.
  # NOTE: While the above statement is true, it's not just the max score
  # with a remainder of 1 that can be hit with 2 2-value problems (and
  # some number of 3-value problems). It's almost all remainder 1 scores
  # that get covered by adding 2 2-value problems (4 = 2+2, 7 = 3+2+2,
  # 10 = 3+3+2+2, etc.). The only scores that can't be hit are 1 because
  # only a 1-value problem can get that score, and the max-1 score that is
  # a multiple of 3 because otherwise we need an extra 3-value problem as
  # mentioned earlier. So as long as the scores 1 and max-1 aren't in the
  # set, we can use 3-value problems up to the max-4 score, then 2 2-value
  # problems. Otherwise, the remainder 1 case works like the remainder 2
  # case.
  #
  # The max score is the important one.
  max_score = max(S)
  # First check if all the scores are multiples of 3 because then we just
  # need a third of the max score in 3-value problems.
  # Turn S into an array to evaluate all elements at once.
  S_array = np.array(S)
  # Use mod to see the remainders.
  remainders = S_array % 3
  # If all remainders are 0, then all scores were even.
  if np.all(remainders == 0):
      # Need only 3-value problems.
      return max_score // 3
  # The max score is a multiple of 3, but there are other scores that
  # are remainder 1, remainder 2, or both.
  elif max_score % 3 == 0:
      # Replace one of the 3-value problems with a 1-value and 2-value
      # problem to cover all scores inbetween.
      return max_score // 3 + 1
  # The max score is a remainder 2.
  elif max_score % 3 == 2:
      # If there are also scores that are remainder 1.
      if np.any(remainders == 1):
          # Need 3-value problems up to the multiple of 3 below the max,
          # then a 2-value problem to cover the max, and a 1-value
          # problem to cover the remainder 1 scores.
          return (max_score - 2) // 3 + 2
      # No remainder 1 scores. Also covers remainder 2 scores because
      # max is remainder 2.
      else:
          # Need 3-value problems up to the multiple of 3 below the max,
          # then a 2-value problem to cover the max.
          return (max_score - 2) // 3 + 1
  # The max score is a remainder 1.
  else:
      # As long as the scores 1 and max-1 aren't in the set, we can
      # use 3-value problems up to the max-4 score, then 2 2-value
      # problems.
      if (1 not in S) and ((max_score - 1) not in S):
          return (max_score - 4) // 3 + 2
      # If there are also scores that are remainder 2 (but not the
      # special case.
      elif np.any(remainders == 2):
          # Need 3-value problems up to the multiple of 3 below the max,
          # then a 1-value problem to cover the max, and a 2-value
          # problem to cover the remainder 2 scores.
          return (max_score - 1) // 3 + 2
      # No remainder 2 scores. Also covers remainder 1 scores because
      # max is remainder 1.
      else:
          # Need 3-value problems up to the multiple of 3 below the max,
          # then a 1-value problem to cover the max.
          return (max_score - 1) // 3 + 1
