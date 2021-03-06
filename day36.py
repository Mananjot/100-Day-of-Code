"""

Question: Hack it

Generate all passwords from the given character set. Given a set of characters generate all possible passwords from them. 
This means we should generate all possible permutations of words using the given characters, with repetitions and also upto a given length.

Sample Input 1
Input : hack_it(['a', 'b'],2)

Sample Output 1
['a', 'b', 'aa', 'ab', 'ba', 'bb']

"""

from itertools import product

def hack_it(chars,length):
  #write your code here
  password = []
  
  for i in range(length):
    for j in  product(chars, repeat = (i+1)):
      password.append(''.join(j))
  return password
  
if __name__ == "__main__":
  chars = ['a', 'b'] 
  print(hack_it(chars,len(chars)))


