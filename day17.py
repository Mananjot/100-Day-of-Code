"""

Question: Swap Linked List

Given a singly linked list and an integer K, reverses the nodes of the
list K at a time and returns modified linked list.
   
Input 1
1 -> 2 -> 3 -> 4 -> 5 -> 6 
K=2

Output 1
2 -> 1 -> 4 -> 3 -> 6 -> 5

NOTE : The length of the list is divisible by K

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
    
  # Growing the list in Backward Direction
  def appendHead(self, val):
    if self.count == 0:
      self.head = ListNode(val)
    else:
      curr = ListNode(val, self.head)
      self.head = curr
    self.count += 1
  def append(self, val):
    if self.count == 0:
      self.head = ListNode(val)
      self.tail = self.head
    else:
      add = ListNode(val)
      self.tail.next = add
      self.tail = add
    self.count += 1
  
  # def append(self, val):
  #   if self.count == 0:
  #     self.head = ListNode(val)
  #   else:
  #     prev = self.head
  #     for _ in range(self.count - 1):
  #       prev = prev.next 
  #     add = ListNode(val)
  #     prev.next = add
  #   self.count += 1
    
  # Empty the Linked List
  def clear(self):
    self.head = None
  
        
class Solution:
    def swapLinkedLists(self, l1: ListNode,key: int) -> ListNode:
      tempSwapList = LinkedList()      # For intermediate reversing of nodes ... will contain only 'key' no. of elements at a time 
      swapList = LinkedList()        
      
      while l1 != None:
        # Swapping 'key' nodes and storing it in tempSwapList
        for _ in range(key):
          tempSwapList.appendHead(l1.val)
          l1 = l1.next
          
        # Appending nodes of tempSwapList to the permanent swapList
        ptr = tempSwapList.head
        for _ in range(key):
          swapList.append(ptr.val)
          ptr =ptr.next
          
        # Clearing tempSwapList to contain other set of reversed values
        tempSwapList.clear()
      return swapList.head
          
          
        
          
          
        
