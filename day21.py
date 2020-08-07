"""
Question: Maximum 2D Column
Write a  program to find maximum of each column of  2d array 

Sample Input -> Output
max_col([[1, 5, 13], [11], [9, 18]]) → [11, 18, 13] 
max_col([[1, 8, 1], [1,21], [9]]) → [9, 21, 1]

"""


import itertools as it
def max_col(test_list):
  # Write your code here
  # Refer Explanation below
  test_list = map(list, it.zip_longest(*test_list, fillvalue = 0))
  res = list(it.starmap(max, test_list))
  return res
if __name__ == "__main__":
  input_list = [[1, 8, 1], [1,21], [9]]
  print(max_col(input_list))


"""

**Explanation of the Code**
1 zip_longest is used to transpose the matrix as we need to find the max of column
2. zip_longest can take no. of iterables as arguments, 
   Note: Here i have also taken fillvalue as argument in order to replace None with 0 
         as the all lists are not of same size and comparison would not be Possible with None
3. zip_longest used can be represented as (iterable1, iterable2, fillvalue = "")
4.zip_longest returns the iterables in different faishon i.e after transposing them

Example --> zip_longest([1,8], [2,7]) returns [1,2] and [8,7]

Role of *: * unzip the list given to it 
Example: 
zip_longest(*test_list) 
=> zip_longest(*[[1, 8, 1], [1,21], [9]])
=>zip_longest([1, 8, 1], [1,21], [9])
Thus it will return [1,1,9] [8,21,None] and [1,None,None]
None is replaced by fillvalue = 0 

Starmap then iterates to the test_list = [[1,1,9]],[8,21,0],[1,0,0]] from zip_longest
and returns max from each of the list inside the list i.e individually from [1,1,9] [8,21,0] and [1,0,0] 
The maximum of each is converted to the list

Note --> test_list = list(map(list, it.zip_longest(*test_list, fillvalue = 0))) 
         After converting test_list to list we will be able to print result
         otherwise printing it will give the address (as done above)
         
"""
