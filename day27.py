"""
Question: Return Vertically

Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.

Sample Input 1
s = "HOW ARE YOU"

Sample Output 1
["HAY","ORO","WEU"]

Explanation1 Each word is printed vertically. 
"HAY"
"ORO"
"WEU"

Sample Input 2
s = "TO BE OR NOT TO BE"

Sample Output 2
["TBONTB","OEROOE","   T"]

Explanation 2 
Trailing spaces is not allowed. 
"TBONTB"
"OEROOE"
"   T"

"""

def return_vertically(input_string):
  #write your code here
  strList = input_string.split(" ")
  maxLength = len(max(strList, key = len))
  
  makeEqual = lambda x: x + " "*(maxLength - len(x))
  strList = list(map(makeEqual, strList))
  
  res = list(map(str.rstrip,map("".join, zip(*strList))))
  return res
  
if __name__ == "__main__":
  input_string = "TO BE OR NOT TO BE"
  print(return_vertically(input_string))


