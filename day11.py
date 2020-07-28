"""

Question: Linked List
Write a Python program to search a specific item in a singly linked list and return true if the item is found otherwise return false.

Sample input 1

items = singly_linked_list()
items.append_item('PHP')
items.append_item('Python')
items.append_item('C#')
items.append_item('C++')
items.append_item('Java')
items.search_item('SQL')


Sample output 1
False

"""

class Node:
    # Singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None
class singly_linked_list:
    def __init__(self):
        # Create an empty list
        self.tail = None
        self.head = None
        self.count = 0
    def append_item(self, data):
        #Append items on the list
        if self.count == 0:
          self.head = Node(data)
        else:
          last_node = self.head
          for _ in range(self.count-1):
            last_node = last_node.next
          add = Node(data)
          # add.next = None     # Not Required --> The class call will declare it add.next as None
          last_node.next = add
        self.count += 1
    def search_item(self, val):
        # Search the list
        curr_node = self.head
        for _ in range(self.count):
          if curr_node.data == val:
            return True
          curr_node = curr_node.next
        return False
          
if __name__ == "__main__":
  items = singly_linked_list()
  items.append_item('PHP')
  items.append_item('Python')
  items.append_item('C#')
  items.append_item('C++')
  items.append_item('Java')
  print(items.search_item('SQL'))
