"""

Question: Recursively getting sum of a nested list

Write a Python program of recursion list sum.

Sample Input 1
grid = [1, 2, [3,4],[5,6]]

Sample Output 1 
21

"""

# Reffered from 
# https://stackoverflow.com/questions/42501002/recursively-getting-sum-of-a-nested-list/42501160

def recursive_sum(input_matrix):
  #write your code here
  if type(input_matrix) != list:
    return input_matrix
  if input_matrix == []:
    return 0
  return recursive_sum(input_matrix[0]) + recursive_sum(input_matrix[1:])

if __name__ == "__main__":
  input_matrix = [1, 2, [3,4],[5,6]]
  print(recursive_sum(input_matrix))
