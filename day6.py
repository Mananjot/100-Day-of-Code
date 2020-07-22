"""

Question: Move Element to End

You're given an array of integers and an integer. Write a function that moves all instance of that integer in the array to the end of the array and returns the array.

Write a function that should perform this in place (i.e , it should mutate the input array) and doesn't need too maintain the order of the other integer.

Time Complexity:
O(n) time | O(1) space,
where n, is the length of the array

Sample Input 1

array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

Sample Output 2

[1, 3, 4, 2, 2, 2, 2] // the number 1, 3, and 4 could be ordered differently


"""

def moveElementToEnd(array, toMove):
    # Write your code here.

    """

    # method 1 --> Creating two separate list
    # time complexity --> O(n) and space complexity --> O(l + m) **check**
    to_move_list =[]          # let final size be l 
    others_list =[]           # let final size be m (note --> l + m = n)
    for i in range(len(array)):
      if array[i] == toMove:
        to_move_list.append(toMove)
      else:
        others_list.append(array[i])
    # return others_list.extend(to_move_list)   #output --> None
    others_list.extend(to_move_list)    # extends manipulates or add elements to same list and return none
    return others_list

    """

    # method 2 --> Swap the elements: move pointer j only if it is equal to toMove
    # i.e move from last element if it toMove
    # time complexity --> O(n) and space complexity --> O(1) **check**

    i = 0
    j = len(array) - 1
    while i < j:
      if array[j] == toMove:     # The order of coditions should not change, examine the sample Input 
        j -= 1
      elif array[i] == toMove:
        array[i], array[j] = array[j], array[i]
        i += 1
      else:
        i += 1
    return array


  # Note --> if conditional statements order is changed then change the code inside it aswell
  
if __name__ == "__main__":
  array =  [2, 1, 2, 2, 2, 3, 4, 2]
  toMove = 2
  print(moveElementToEnd(array, toMove))
