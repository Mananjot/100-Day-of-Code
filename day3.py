"""
Question: Smallest Difference  
 
Write a function that takes in two non-empty arrays of integers, find the pair of numbers (one from each array) whose absolute difference is closet to zero, and returns an array containing these two numbers, with the numbsers, with the number from the first array in the first position.

You can assume that there will only be one pair of numbers with the smallest difference.

Sample Input 1
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

Sample Output 1
[28, 26]

Optimal Solution:

O(nlog(n)) + O(mlog(m) + O(m+n))
where,
n is the size of arrayOne
m is the size of arrayTwo

"""

"""
time complexity --> O(n^2) | space complexity --> O(1)
 
def smallestDifference(arrayOne, arrayTwo):
  # Write your code here
  n, m = len(arrayOne), len(arrayTwo)         
  min = abs(arrayOne[0] - arrayTwo[0])
  result = [arrayOne[0], arrayTwo[0]]
  for i in range(n):
    for j in range(m):
      if abs(arrayOne[i] - arrayTwo[j]) < min:
        min = abs(arrayOne[i] - arrayTwo[j])
        result = [arrayOne[i], arrayTwo[j]]
  return result
"""

# time complexity --> O(nlogm) | space complexity --> O(1)

def smallestDifference(arrayOne, arrayTwo):
  # Write your code here
  n, m = len(arrayOne), len(arrayTwo)         
  arrayOne.sort()
  arrayTwo.sort()
  min = abs(arrayOne[0] - arrayTwo[0])
  result = [arrayOne[0], arrayTwo[0]]
  for i in range(n):
    j = 0
    k = m - 1
    while j < k:
      if abs(arrayOne[i] - arrayTwo[j]) > abs(arrayOne[i] - arrayTwo[k]):
        j += 1
      else:
        k -= 1
    if abs(arrayOne[i] - arrayTwo[k]) < min:
      min = abs(arrayOne[i] - arrayTwo[k])
      result = [arrayOne[i], arrayTwo[k]]
  return result
        
if __name__ == "__main__":
  arrayOne = [-1, 5, 10, 20, 28, 3]
  arrayTwo = [26, 134, 135, 15, 17]
  print(smallestDifference(arrayOne, arrayTwo))
