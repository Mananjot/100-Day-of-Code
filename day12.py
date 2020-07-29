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
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.count = 0
  def append(self, val):
    if self.count == 0:
      self.head = ListNode(val)
    else:
      pre_node = self.head
      for _ in range(self.count - 1):
        pre_node = pre_node.next
      self.tail =  ListNode(val)
      pre_node.next = self.tail
    self.count += 1
    
  def del_tail(self):
    pre_node = self.head
    for _ in range(self.count - 2):
      pre_node = pre_node.next
    pre_node.next = None
    self.tail = pre_node
    self.count -= 1
      
    
  def display(self):
    curr = self.head
    for _ in range(self.count - 1):
      print(curr.val, end =" -> ")
      curr = curr.next
    print(self.tail.val)
      

# The code runs absolutly fine if we take array as input and then convert it to the list using ListNode class then process the lists
# The Test cases failed because the linked lists are defined at the backend where the number is converted to linked list and passed to the
# addTwoNumbers Function and function used at the backend don't have attributes that i have used in my class  
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
      carry = 0
      result = []
      while l1.count > 0 and l2.count > 0:
        a = l1.tail.val + l2.tail.val + carry
        if a > 9:
          a -=10
          carry = 1
        else:
          carry = 0
        l1.del_tail()
        l2.del_tail()
        result.append(a)
     
      for i in range(l1.count, 0, -1):
        result.append(l1.tail.val)
        l1.del_tail()
      for i in range(l2.count, 0, -1):
        result.append(l2.tail.val)
        l2.del_tail()
      if carry == 1:
        result.append(1)
      final_result = LinkedList()
      n = len(result)
      for i in range(n-1, -1,-1):
        final_result.append(result[i])
      return final_result.display()
        
a1 = [7,2,4,3]
a2 = [5,6,4]

# a1 = [3,4,5,2,1,8,1]
# a2 = [6,7,9,2]

# a1 = [4,8,5,7]
# a2 = [7,8,9,1]


l1 = LinkedList()
l2 = LinkedList()

for i in range(len(a1)):
  l1.append(a1[i])
  
for i in range(len(a2)):
  l2.append(a2[i])

# l1.display()
# l2.display()


ans = Solution()
print(ans.addTwoNumbers(l1,l2))

