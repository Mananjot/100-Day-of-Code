"""
Question: Check Palindrome

Function to check if a singly linked list is a palindrome
Given a singly linked list of characters, write a function that returns True if the given list is a palindrome, else False.


Sample input
("r" -> "a" -> "d" -> "a" -> "r" )

Sample output
True

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Traversing the list and saving the all characters into a stack (list)
# Again traversing the list and checking the topmost element i.e last character of string 
# by poping it out with first element of linked list
class Solution:
    def checkPalindrome(self, l1: ListNode):
      stack = []
      head_node = l1              # Saving the head_node to return to first element after 'Going through '  
      while l1 != None:
        stack.append(l1.val)
        l1 = l1.next

      l1 = head_node		 # Return back to first element		
      while l1 != None:
        char = stack.pop()
        if l1.val != char:
          return False
        l1 = l1.next
      return True  
        
