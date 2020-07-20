"""

Question: Four Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.

The function should find all quadruplets in the array that sum up to the largest sum and return a two dimensional array of all these
quadruplets in no particular order.

This is the last of its kind, I hope you would have understood the concept of storing complements in the set / dictionary or after sorting the list we can use two pointers to decide whether to decrement / increment the pointers. This problem also works on the similar principle, so don't get trapped into the 4 loop Naive Solution.

Sample Input 1
array = [7,6,4,-1,1,2]
targetSum = 16

Sample Output 2 		// the quadruplets could be ordered differently
[[7, 6, 4, -1], [7, 6, 1, 2]]

Optimal Space & Time Complexity:
Average: O(n^2) time | O(n^2) space - where n is the length of the input arrayTwo
Worst: O(n^3) time | O(n^2) space - where n is the length of the input array

"""

def fourNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    n = len(array)
    result = []
    for idx1 in range(0,n):
      num1 = array[idx1]
      temp_target_1 = targetSum - num1
      for idx2 in range(idx1 + 1, n):
        num2 = array[idx2]
        start = idx2 + 1
        end = n - 1
        temp_target_2 = temp_target_1 - num2
        while start < end:
          if array[start] + array[end] == temp_target_2:
            result.append([num1, num2, array[start],array[end]])
            start += 1
          elif array[start] + array[end] < temp_target_2:
            start += 1
          else:
            end -= 1
    return result
  
if __name__ == "__main__":
  array = [7,6,4,-1,1,2]
  targetSum = 16
  output = fourNumberSum(array, targetSum)
  print(output)
  
