"""

Question: Return Diagonal

Given a matrix of N x M elements (N rows, M columns), return all elements of the matrix in diagonal order as shown in the below image.
Example:

Sample Input 1
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Sample Output 1
[1,2,4,7,5,3,6,8,9]

Explanation 1
Will share image in whatsapp group

Note:
The total number of elements of the given matrix will not exceed 10,000.

"""

def return_diag(input_matrix):
  #write your code here
  n = len(input_matrix)
  m = len(input_matrix[0])  # add condition to return [] if input_matrix is empty i.e n = 0
  diagonalUp = True	    # Considering moving up diagonal initially
  i = j = 0
  res = [input_matrix[i][j]] 

  for _  in range(0,m*n-1):
    # For Moving in diagonal going up
    if diagonalUp == True:
      # Addressing Boundary Conditions
      if j + 1 >= m : 	# if elif Position Should not be changed, if changed index out of bound error for Top Right element
        i += 1
        diagonalUp = False
      elif i - 1 < 0:
        j += 1
        diagonalUp = False
      # Moving in a diagonal going up
      else:
        i = i - 1 
        j = j + 1

    # For Moving in diagonal going down
    else: 
      # Addressing Boundary Conditions
      if i + 1 >= n:
        j += 1
        diagonalUp = True
      elif j - 1 < 0:
        i += 1
        diagonalUp = True
      # Moving in a diagonal going down
      else:
        i += 1
        j -= 1
    res.append(input_matrix[i][j])
  return res
if __name__ == "__main__":
  input_matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
  ]
  print(return_diag(input_matrix))




