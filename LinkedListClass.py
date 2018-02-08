# Script text here
from random import randint

class Node: 
    def __init__(self, cargo=None, next=None):
        self.car = cargo
        self.cdr = next
    
    def __str__(self):
        return str(self.car)


def printList(node):
    while node:
        print node,
        node = node.cdr
    print

def printBackward(list):
    if list == None:
        return 
    head = list 
    tail = list.cdr
    printBackward(tail) 
    print head,
        
def remove(list):
    if list == None:
        return 
    first = list 
    second = list.cdr
    # make the first node refer to the third 
    first.cdr = second.cdr
    # separate the second node from the rest of the list 
    second.cdr = None 
    return second 

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.cdr = node2
node2.cdr = node3
node3.cdr = node4
print node1
print node2
print node3
printList(node1)
node = Node(5)