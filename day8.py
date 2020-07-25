"""

Question: Longest Peak

Given an array arr[] with N elements, the task is to find out the longest sub-array which has the shape of a mountain.
The Longest Peak consists of elements that are initially in ascending order until a peak element is reached and beyond the peak element all other elements of the sub-array are in decreasing order.

Sample Input 1
arr = [2, 2, 2]
 
Sample Output 1
0 

Explanation 1 
No sub-array exists that shows the behaviour of a mountain sub-array.

Sample Input 2 
arr = [1, 3, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5] 

Sample Output 2
11

Explanation 2
There are two sub-arrays that can be considered as mountain sub-arrays. The first one is from index 0 – 2 (3 elements) and next one is from index 2 – 12 (11 elements).  As 11 > 2, our answer is 11.

"""

def LongestPeak(a): 
  # Write your code here
  n = len(a)
  result = temp_result = 0           # temp result help us to avoid use of list
  is_asc = True
  for i in range(n-1):
    if a[i] < a[i+1] and is_asc:
      temp_result += 1
    elif a[i] > a[i + 1]:
      is_asc = False
      temp_result += 1
    elif a[i] < a[i+1] and not is_asc:
      if temp_result > result:
        result = temp_result + 1    # 1 is added because comparison of two will count 1 element and when comparison of 3 will count 2 elements 
      temp_result = 1
      is_asc = True
  # To check the last mountain peak we are using same logic as last elif again as it will not 
  # run for the last peak (because no peak is ascended after that)
  # Also writing temp_result > result prevent result = 1 for [2, 2, 2] like input
  # As temp_result = result = 0 
  if temp_result > result:   
    result = temp_result + 1

  return result

  


if __name__ == "__main__":
  d = [1, 3, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5]  

  print(LongestPeak(d)) 
