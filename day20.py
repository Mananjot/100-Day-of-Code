"""

Question: Remove Zeroes From IP address
Write a  program to remove leading zeros following "." from an IP address.

Sample Input 1 
"216.08.094.196"

Sample Output 1 
"216.8.94.196"

Sample Input 2 
"016.08.0904.96"

Sample Output 2
"016.8.904.96"

"""
import re
import re

def remZero(ip_addr):
  # write your code here
  # Replaces sequence ".0" with "." in ip_addr, "\" removes the metacharacter behaviour of ".", 
  # "." otherwise represents all alphanumeric characters 
  # "+" is to handle leading 0's, "*" will do the same but "+" is more efficient
  result = re.sub("\.0+",'.',ip_addr)   
  return result
  
if __name__ == "__main__":
  ip = "016.08.0904.96"
  print(remZero(ip))



