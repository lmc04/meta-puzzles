# Write any import statements here

def getWrongAnswers(N: int, C: str) -> str:
  # Write your code here
  # Assuming C is of length N because you know the correct answer for each question.
  # Assuming only characters in C are 'A' and 'B'.
  wrong_list = ['A' if C[i] == 'B' else 'B' for i in range(N)]
  # Combine list of strings into one string without any other characters added.
  return ''.join(wrong_list)
