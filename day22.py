"""

Question: Get Dictionary Value

Given a dictionary with nested dictionaries as values, extract all the values with of particular key.

Sample Input 1
test_dict = {
	    ‘sup’: {“a” : 7, “b” : 9, “c” : 12}, 
	    ‘is’ : {“a” : 15, “b” : 19, “c” : 20},
	    ‘best’:{“a” : 5, “b” : 10, “c” : 2}
	    } 
temp = “b”

Sample Output 1
[9, 10, 19]

Explanation 1
All values of “b” key are extracted.

Sample Input 2 
test_dict = {
            ‘sup’: {“a” : 7, “b” : 9, “c” : 12},
            ‘is’ : {“a” : 15, “b” : 19, “c” : 20}, 
            ‘best’:{“a” : 5, “b” : 10, “c” : 2}
	    }
temp = “a”

Sample Output 2
[7, 15, 5]

Explanation 2
All values of “a” key are extracte

"""

def get_key(input_dict,key):
  #write your code here
  res = []
  for value in input_dict.values():   # Iterating the values of input_dict which themselves are the Dictionary
    if key in value.keys():           # As value is also a dictionary, so checking that given key is present in value or not
      res.append(value[key])          # Do nothing if given key is not present
  return res
if __name__ == "__main__":
  input_dict = {
           'sup': {"a" : 7, "b" : 9, "c" : 12}, 
	   'is' : {"a" : 15, "b" : 19, "c" : 20}, 
	   'best':{"a" : 5, "b" : 10, "c" : 2}
           }
  key = "c"
  print(get_key(input_dict,key))

