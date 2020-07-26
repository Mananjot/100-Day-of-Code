"""

Question: Ceasar Cipher Encryptor

Given a non-empty string of lowercase letters and a non-negative integer representing a key, Write a function that returns a new string obtained by shifting any letter in the input string by k positions in the alphabet, where k is the key. Note that letters should "wrap" around the alphabet; in other words, the letter "z" shifted by one returns the letter "a"

Sample Input 1
string = "xyz"
key = 2


Sample Output 1
"zab"

Optimal Space & Time Complexity
O(1) & O(n), where n is the length of the input string. 

"""

def caesarCipherEncryptor(string, key):
    # Write your code here.
    str_length = len(string)
    cipher_txt = ""
    for i in range(str_length):
      plain_txt_idx = ord(string[i]) - 97         # Converting to ascii code and then to the index as per English language
      cipher_txt_idx = (plain_txt_idx + key) % 26 # Adding Key to it and finding the remainder for rap up
      cipher_txt += chr(cipher_txt_idx + 97)      # Converting back to string first by taking it to ascii value from English index
    return cipher_txt
    
  
      
string = "xyz"
key = 2
print(caesarCipherEncryptor(string, key))
