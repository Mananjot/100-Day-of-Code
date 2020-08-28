"""

Question: Strictly Increasing

Print all n-digit strictly increasing numbers
Given number of digits n in a number, print all n-digit numbers whose digits are strictly increasing from left to right.

Sample Input 1 
n = 2

Sample Output 2  
[
 '01', '02', '03', '04', '05', '06', '07', '08', '09', 
 '12', '13', '14', '15', '16', '17', '18', '19', '23', 
 '24', '25', '26', '27', '28', '29', '34', '35', '36', 
 '37', '38', '39', '45', '46', '47', '48', '49', '56', 
 '57', '58', '59', '67', '68',   '69', '78', '79', '89'
]

Sample Input 2 
n = 1

Sample Output 2
['01', '02', '03', '04', '05', '06', '07', '08', '09']

"""

# Reference: https://github.com/cahuja1992/MyTutorials/blob/master/%23100daysOfCode/day35.py

def recursion(n, num, tempRes,res):
  if n == 0:
    res.append(tempRes)
    return
  for i in range(num, 10):
    recursion(n-1, i + 1, tempRes + str(i),res)

def strictly_increasing(input_number):
  #write your code here
  #return all possible outputs in a list
  n = input_number
  res = []
  if n == 1:
    for i in range(1,10):
      res.append("0" + str(i))
    return res
  recursion(n, 0, "",res)
  return res

if __name__ == "__main__":
  input_number = 2
  print(strictly_increasing(input_number))





