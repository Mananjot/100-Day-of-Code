"""

Question: Pop Linked List
Given a linked list, remove the n-th node from the end of the list and return its head.

Sample Input 1
Given linked list: 1->2->3->4->5
n = 2.

Sample Output 1
1->2->3->5

Explanation 1
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note: Given n will always be valid.

"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
      # Calculating the Length of the Linked List
      length = 0
      curr = head
      while curr != None:
        length += 1
        curr = curr.next
      
      # Finding the index of node to be deleted 
      # using n - r + 1 to find the node to be removed from begining (+1 not included to get index)
      idx = length - n
      
      # Checking if head is to be removed
      if idx == 0:
        head = head.next     # Shifting head to node at index 1
        return head
      
      # getting to the node previous to idx i.e idx - 1 
      prev = head
      for _ in range(1, idx):         # can be written as idx - 1, one less because prev is present at head i.e one move is already moved 
        prev = prev.next              # For eg: to remove idx = 1 no need to move head
      prev.next = prev.next.next     
      return head
      
      
        

    
