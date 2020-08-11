"""
Question: Find Target

Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:
1. Integers in each row are sorted from left to right.
2. The first integer of each row is greater than the last integer of the previous row.

Sample Input 1
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3

Sample Output 1
True


Sample Input 2
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13

Sample Output 2
False
"""

"""
# Solution --> 1
# Brute Force Method --> O(n^2) time complexity
def find_target(input_matrix,target):
  #write your code here
  m = len(input_matrix)
  n = len(input_matrix[0])
  for i in range(m):
    for j in range(n):
      if input_matrix[i][j] == target:
        return True
  return False
"""

"""
# Solution --> 2
#time complexity --> O(m + n) 
def find_target(input_matrix,target):
  #write your code here
  m = len(input_matrix)
  n = len(input_matrix[0])
  i = 0
  j = n - 1   
  
  # Start iterating from the first row and last column
  while i < m and j > -1:
    if input_matrix[i][j] == target:
      return True
    elif input_matrix[i][j] < target:     # If target is greater than the current element jump to next row
      i +=1
    else:                                 # If target is less than the current element start jumping to the previous column within same row
      j -= 1
  return False
"""

"""
# Solution --> 3
The Problem is solved in the same manner as for searching in 1D list using binary search
Manipulation has been done in the indices of input_matrix to access the elements

Time Complexity --> O(logm + logn)
"""

def find_target(input_matrix,target):
  #write your code here
  m = len(input_matrix)                     # No. of Rows
  n = len(input_matrix[0])                  # No. of Columns
  
  low = 0                                   # Index of the first element 
  high = m * n - 1                          # Index of the last element as in 1D list

  while low <= high:
    mid_column = (low + high) // 2          # Gives the index of the middle element as in 1D List
    mid_row = mid_column // n               # Gives the Row of the middle element (mid index is divided by no. of columns). This is the additional part for 2D List
    
    # To get the index of mid coloumn in 2D List take remainder with no. of elements in a row (i.e no. of columns) --> additional 
    if input_matrix[mid_row][mid_column%n] == target:
      return True
    
    if input_matrix[mid_row][mid_column%n] > target:
      high = mid_column - 1
  
    elif input_matrix[mid_row][mid_column%n] < target:
      low = mid_column + 1
     
  return False

if __name__ == "__main__":
  input_matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
  ]
  target = 3
  print(find_target(input_matrix,target))


