"""

Ques: Add Linked List

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Sample input:
(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)

Sample output
7 -> 8 -> 0 -> 7

"""

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

# Class to build the linked list that is to be returned as result
class LinkedList:
  def __init__(self):
    self.head = None
    self.count = 0
  
  # It creates our linked list. Actually it grows in backward direction adding head each time
  def changeHead(self,val):
    if self.count == 0:
      self.head = ListNode(val)
    else:
      curr = ListNode(val, self.head)
      self.head = curr
    self.count += 1
        
class Solution:
  def __init__(self):
    # Declaring the Linked List to store the result
    self.sumList = LinkedList() 
  
  # A method that runs recursively till it reaches the end of the list (least significant digit)
  # And after computing the sum returns the carry to the calling function
  # The carry than is added with previous two nodes (that were already stored in recursion stack) 
  # At the every returning step the sum calculated is appended to 'sumList' and making that as head every time
  # So at last the head of the list is at the most significant digit of the answer
  def computeCarry(self,num1, num2, carry):
    if num1.next == num2.next == None:
      sum = num1.val + num2.val
      if sum >= 10:
        sum -= 10
        carry = 1
      self.sumList.changeHead(sum)
      return carry
    else:
      sum = self.computeCarry(num1.next, num2.next, carry) + num1.val + num2.val
      if sum >= 10:
        sum -= 10
        carry = 1
      else:
        carry = 0
      self.sumList.changeHead(sum)
      return carry
      
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    l1Length = 0
    l2Length = 0
    l1Head = l1
    l2Head = l2
    
    # Counting Lengths of Linked List
    while l1Head != None:
      l1Length += 1
      l1Head = l1Head.next           
        
    while l2Head != None:
      l2Length += 1
      l2Head = l2Head.next  
      
    # Checking the lengths of the linked list and adding 0's to the smaller linked list
    if l1Length < l2Length:
      for _ in range(l2Length - l1Length):
        curr = ListNode(0, l1)
        l1 = curr
    elif l1Length > l2Length:
      for _ in range(l1Length - l2Length):
        curr = ListNode(0, l2)
        l2 = curr
        
    # Calling the recursive function
    carry = self.computeCarry(l1, l2, 0)
    
    # Checking if there is carry even if the lists are added if so add it as most significant digit
    if carry == 1:
      self.sumList.changeHead(1)
    
    return self.sumList.head
        
""" 
    
Note: The Adding 0's to the list can be avoided by first trimming longer linked list and adding 
the same length of list and then appending the longer list to result
But the carry returned in the last addition may become difficut to handle in some cases
Example --> 9999123 + 921
Step 1 -->  123
            921
tempResult= 044
Step 2 carry = 1 + 9 = 10 --append 0-- 0044
Step 3 carry = 1 + 9 = 10 --append 0-- 00044
Step 4 carry = 1 + 9 = 10 --append 0-- 000044
Step 5 carry = 1 + 9 = 10 --append 0-- 0000044
Step 6 --append carry = 1 -- 10000044

Though this is to be carried in loop/recursively but the code the code becomes repetative
as we will require to do the same kind of computation again that we have already done to compute 123 + 921

It may be simple to add for the case like 12123 + 921 = 13044 as no carry is generated by the the remaining elements.
But the code need to be same for both :)

"""



