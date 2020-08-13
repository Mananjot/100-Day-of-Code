"""
Question: Anagrams

Given two strings s and t , write a function to determine if t is an anagram of s.

Sample Input 1
s = "anagram", t = "nagaram"
Sample Output 1
True

Sample Input 2
s = "rat", t = "car"
Sample Output 2
False
"""

# Time Complexity --> nlogn + mlogm
def check_anagram(sentence_1,sentence_2):
  #write your code here
  sentence_1 = (sentence_1.lower()).replace(" ", "")
  sentence_2 = (sentence_2.lower()).replace(" ", "")

  if sorted(sentence_1) == sorted(sentence_2):
    return True
  else:
    return False
    
if __name__ == "__main__":
  sentence_1 = "aabc"
  sentence_2 = "abcd"
  print(check_anagram(sentence_1,sentence_2))
