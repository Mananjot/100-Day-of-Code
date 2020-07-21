def bool2str(m_bool):
  if m_bool:
    return 'true'
  else:
    return 'false'
    
def isValidSubsequence(array, sequence):
    is_valid = False
    
    # Write your code here.
    n = len(array)
    m = len(sequence)
    i = j = 0
    while i < n and j < m:
      if sequence[j] == array[i]: 
        j += 1                            				# see the variation in the comment below
      i += 1

    # if we competely traverses 2nd array than it is a subsequence 
    # here j == m and not equal to index m - 1 bcoz after matching last element j is again incremented
    if j == m:              		
      is_valid = True
    return bool2str(is_valid)

if __name__ == "__main__":
  array = [ 5, 1, 22, 5, 6, -1, 8, 10]
  subsequence = [1, 6, -1, 10]
  print(isValidSubsequence(array, subsequence))

"""
def isValidSubsequence(array, sequence):
  while i < n and j < m:
    if sequence[j] == array[i]:
      i += 1
      j += 1
    else:
      i += 1
"""
