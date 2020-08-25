"""

Question: Sum Tree

You are given a binary tree in which each node contains an integer value.Find the number of paths that sum to a given value.The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Sample Input 1
root = [10,5,-3,3,2,None,11,3,-2,None,1]
sum = 8

Sample Output 1
3

Explanation 1

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1


The paths that sum to 8 are:
1. 5 -> 3
2. 5 -> 2 -> 1
3. -3 -> 11

"""

def sum_tree(input_matrix,sum_val):
  #write your code here
  count = [0]
  def path(idx, sum):
    if sum == sum_val:
      count[0] += 1
    if 2*idx + 1 < len(input_matrix) and input_matrix[2*idx + 1] != None:
      path(2*idx + 1, sum + input_matrix[2*idx + 1])
    if 2*idx + 2 < len(input_matrix) and input_matrix[2*idx + 2] != None:
      path(2*idx + 2, sum + input_matrix[2*idx + 2])
      
  for i in range(len(input_matrix)):
    path(i, input_matrix[i])
  return count[0]

if __name__ == "__main__":
  input_matrix = [10,5,-3,3,2,None,11,3,-2,None,1]
  sum_val = 8
  print(sum_tree(input_matrix,sum_val))

