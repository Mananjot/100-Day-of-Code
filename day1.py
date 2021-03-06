"""
Question: Two Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum upto the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array. 

Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum.You can assume that there will be at most one pair of numbers summing up to the target sum.

Sample Input 1
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

Sample output 1
[-1, 11] // the numbers could be in reverse order

Optimal Solution: O(n) time | O(n) space - where n is the length of the input array.

"""

def twoNumberSum(array, targetSum):
    """
      Write your code here, return result while removing pass
      
    """
    for i in range(len(array)):
      diff = targetSum - array[i]
      if diff in array and diff != array[i]:
        return [array[i],diff]

if __name__=='__main__':
  print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6],10))
