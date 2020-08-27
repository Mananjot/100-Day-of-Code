"""

Question: Palindrome Recursion

Given a string, find all possible palindromic partitions of given string. The idea is to go through every substring starting from first character, check if it is palindrome. If yes, then add the substring to solution and recur for remaining part.

Sample Input 1
nitin

Sample Output 1
['n i t i n', 'n iti n', 'nitin']

"""

# Reference: https://www.geeksforgeeks.org/python-remove-square-brackets-from-list/
def isPalindrome(string, s ,e): 
  while s < e: 
    if string[s] != string[e]: 
      return False
    s += 1
    e -= 1
  return True
  
def allPalPartUtil(res, curr, start, n, string): 
  if start >= n: 
    x = curr.copy() 
    res.append(x) 
    return
  for i in range(start, n): 
    if isPalindrome(string, start, i):
      curr.append(string[start:i + 1])
      allPalPartUtil(res, curr, i + 1, n, string)
      curr.pop() 
      
def recursive_palindrome(string):
  #write your code here
  n = len(string)
  res = []
  curr = []
  allPalPartUtil(res, curr, 0, n, string)
  res = list(map(" ".join, res))
  return res
  
if __name__ == "__main__":
  input_string = "nitin"
  print(recursive_palindrome(input_string))




