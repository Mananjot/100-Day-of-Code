"""
Question: Remove Loop in Linked List

You are given a linked list of N nodes. The task is to remove the loop from the linked list, if present.

Input:
First line of input contains number of testcases T. 
T testcases follow. For each testcase, first line of input contains length N  of the linked list and next line contains N data of the linked list.  The third line contains the position of the node(from head) to which the  last node will get connected. If it is 0 then there is no loop.

Output:
For each testcase, in a new line, 1 will be printed if loop is removed and the list still has all N nodes connected to it, else 0 will be printed.

User Task:
Your task is to complete the function removeLoop(). The  only argument of the function is head pointer of the linked list. Do  not print anything. Simply remove the loop in the list (if present)  without disconnecting any nodes from the list.

Constraints:
1 <= T <= 102
1 <= N <= 104

Expected time complexity : O(n)
Expected auxiliary space : O(1)

Input 1
2
3
1 3 4
2
4
1 8 3 4
0

Output 1
1
1

Explanation 1
Testcase 1: In the first test case N = 3.The linked  list with nodes N = 3 is given. Here, x = 2 which means last node is  connected with xth node of linked list. Therefore, there exists a loop. 
Testcase 2: N = 4 and x = 0, which means lastNode->next = NULL, thus the Linked list does not contains any loop.

"""

'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''
# The Solution might not be applicable if loop begins at head
def removeLoop(head):
  # code here
  # remove the loop without losing any nodes
  fast = head.next
  slow = head

  # Checking if there is a loop or not
  while slow != fast:
    if fast == None or fast.next == None:
      return 
    slow = slow.next
    fast = fast.next.next
  
  # To remove loop, move one pointer to the head node 
  slow = head

  # In order to remove the loop we must point to the node previous to the Node where the loop begins
  # So checking by slow.next != fast.next and not by slow != fast 
  # this would be the case if we have to determine the starting node of the loop
 
  while slow.next != fast.next and fast.next != slow :
    slow = slow.next
    fast = fast.next
  fast.next = None              # Specifying the Last node as None to break loop


"""

Note : The second condition i.e fast.next != slow is added to prevent the loop to run infinitely
This could be the case when node from where the linked list loop begins and head (slow) are next to each other
or after entering the loop in the linked list fast and slow comes next to each other

Example 1 
1 -> 3 -> 4  node from where loop starts (Loop Node) --> 2 (its value is 3)
fast node and head (slow) now will be next to each other after loop exitance is checked
so  there will be infinite loop but second will terminate it

Example 2
1 -> 3 -> 5 -> 7 Loop Node --> (Value 3)
The fast and slow are not next to each other when loop existance checking ends but
The fast and slow are next to each other when  they enter the loop of linked list
So 2nd condition will prevent from entering the infinite loop

"""
  
class Node:

  def __init__(self,val):
    self.next=None
    self.data=val

class linkedList:

  def __init__(self):
      self.head=None
      self.tail=None
  
  def add(self,num):
      if self.head is None:
          self.head=Node(num)
          self.tail=self.head
      else:
          self.tail.next=Node(num)
          self.tail=self.tail.next
  
  def isLoop(self):
      if self.head is None:
          return False
      
      fast=self.head.next
      slow=self.head
      
      while slow != fast:
          if fast is None or fast.next is None:
              return False
          fast=fast.next.next
          slow=slow.next
      
      return True
  
  def loopHere(self,position):
      if position==0:
          return
      
      walk=self.head
      for _ in range(1,position):
          walk=walk.next
      self.tail.next=walk
  
  def length(self):
      walk=self.head
      ret=0
      while walk:
          ret+=1
          walk=walk.next
      return ret

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=tuple(int(x) for x in input().split())
        pos=int(input())
        
        ll = linkedList()
        for i in arr:
            ll.add(i)
        ll.loopHere(pos)
        
        removeLoop(ll.head)
        
        if ll.isLoop() or ll.length()!=n:
            print(0)
            continue
        else:
            print(1)

# } Driver Code Ends

