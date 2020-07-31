"""

Question: Merge Linked List

Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.

Sample Input 1
5 -> 8 -> 20 
4 -> 11 -> 15

Sample Output 1
4 -> 5 -> 8 -> 11 -> 15 -> 20

"""
# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val         
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = ListNode()      
    self.count = 0
  def append(self, val):
    prev = self.head
    for _ in range(self.count):
      prev = prev.next
    appendNode = ListNode(val)
    prev.next = appendNode
    self.count += 1
    
class Solution:
  def addTwoLinkedLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    merged_list = LinkedList()   # Create the psuedo node with val = 0 and next = None
    
    # Traversing completely one of the two linked list 
    # Comparing each node of linked list and appending the smaller node to new list
    while l1 != None and l2 != None:
      if l1.val < l2.val:
        merged_list.append(l1.val)
        l1 = l1.next
      elif l1.val > l2.val:
        merged_list.append(l2.val)
        l2 = l2.next
      else:
        merged_list.append(l1.val)
        l1 = l1.next
        l2 = l2.next
    
    # Traversing remaining nodes of l1 and appending to the merged list
    while l1 != None:
      merged_list.append(l1.val)
      l1 = l1.next
    
    # Traversing remaining nodes of l2 and appending to the merged list
    while l2 != None:
      merged_list.append(l2.val)
      l2 = l2.next
    
    # Returning the node(head) next to the psuedo head
    return merged_list.head.next
    
    

