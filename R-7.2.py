ANSWER :-

Step 01 - Algorithm:-

(Both the linked lists are singly linked list and only reference to first node is provided. So any kind of access other than linear way starting from first node, is not possible)

So our algorithm for concatenating two singly linked lists is given below -

concatLL(firstLinkedList: Singly linked list, secondLinkedList: Singly linked list)

initialize an empty singly linked list, new_list // merged linked list will be stored in new_list

start from the head node in the first linked list, until end of the list is reached

add elements from the first linked list to the end of the new_list

start from the head node in the second linked list, until end of the list is reached

add elements from the second linked list to the end of the new_list

Step 02 - Python implementation

(Python 3.8 64-bit)

class Node:

"""Represents a node of a singly linked list."""

def _init_(self, data, next=None):

"""Instantiates a node of a singly linked list which by default points to None."""

self.data = data

self.next = next

class SLL:

"""Represents a a singly linked list."""

def _init_(self):

"""Instantiates an empty singly linked list."""

self.head = None

def add(self, data):

"""Add a node in the end of the linked list."""

if self.head is not None:

temp = self.head

while temp.next is not None:

temp = temp.next

temp.next = Node(data, None)

else:

self.head = Node(data, None)

def printList(self):

"""Add a node in the end of the linked list."""

if self.head is not None:

temp = self.head

while temp is not None:

print(temp.data, end=" ")

temp = temp.next

else:

print("List is empty")

def concatLL(firstLinkedList, secondLinkedList):

newList = SLL()

temp = firstLinkedList.head

while temp is not None:

newList.add(temp.data)

temp = temp.next

temp = secondLinkedList.head

while temp is not None:

newList.add(temp.data)

temp = temp.next

return newList

print("First list is -", end=" ")

firstLinkedList = SLL()

firstLinkedList.add(5)

firstLinkedList.add(6)

firstLinkedList.add(7)

firstLinkedList.printList()

print("\nSecond list is -", end=" ")

secondLinkedList = SLL()

secondLinkedList.add(1)

secondLinkedList.add(2)

secondLinkedList.add(3)

secondLinkedList.printList()

print("\nConcatenated list is -", end=" ")

concatenatedList = concatLL(firstLinkedList, secondLinkedList)

concatenatedList.printList()
