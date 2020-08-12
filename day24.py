"""
Question: Do as Romans do

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty-seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral. 
Input is guaranteed to be within the range from 1 to 3999.

Sample Input 1
3

Sample Output 1 
III

Sample Input 2
4

Sample Output 2
IV

Sample Input 3
9

Sample Output 3
IX

Sample Input 4
58

Sample Output 4
LVIII

Explanation 
L = 50, V = 5, III = 3.

Sample Input 5
1994

Sample Output 5
MCMXCIV

Explanation
M = 1000, CM = 900, XC = 90 and IV = 4.
"""

def num_conversion(input_number):
  #write your code here
  roman = {
    1 : 'I', 4 : 'IV', 5 : 'V', 9 : 'IX', 10 : 'X', 40 : 'XL', 50 : 'L',
    90 : 'XC', 100 : 'C', 400 : 'CD', 500 : 'D', 900 : 'CM', 1000 : 'M',
  }
  res = ""
  rem = input_number
  while rem > 0:
    n = len(str(rem))
    place = 10**(n-1)
    faceValue = rem // place
    placeValue = faceValue*place
    
    if placeValue in roman.keys():
      base = placeValue
      rem %= place
      res += roman[base]
      
    else:
      if faceValue > 1 and faceValue < 4:
        base = place
        rem %= place
        res += roman[base]*faceValue
      elif faceValue >= 6 and faceValue < 9:
        base = place * 10 // 2
        rem -= base
        res += roman[base]
  return res
  
if __name__ == "__main__":
     input_number = 88
     print(num_conversion(input_number))

