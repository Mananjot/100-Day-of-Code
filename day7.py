"""
Question: Monotonic Array

Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.
An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non -decreasing.

Sample Input 1
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

Sample Output 1
True

Time Complexity:  
O(n) time | O(1) space, where n is the length of the array

"""

def monoArray(array):
    # Write your code here.
    # Intial comparison array[0] > array[1] is not made in order to 
    # pass any test that have first two elements same 
    n = len(array)
    inc_count = dec_count  = 0   # Increasing order count, Decreasing order count
    for i in range(n-1):
      if array[i] > array[i+1]:
        dec_count += 1
        if inc_count != 0:
          return False
      elif array[i] < array[i+1]:  # not using else bcoz it will include == as well
        inc_count += 1
        if dec_count != 0:
          return False
    return True
        


if __name__ == "__main__":
  array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
  print(monoArray(array))
  
# If intial comparison method is used then we can run a loop and check that 
# is there any element that complement the initial comparison if so return false
