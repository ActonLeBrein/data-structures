class Node:
    def __init__(self, data):
        self.data=data 
        self.next=None

def is_circular(head):
	slow = head
	fast = head
	while fast != None:
		slow = slow.next
		if fast.next != None:
			fast = fast.next.next
		else:
			return False
		if slow is fast:
			return True
	return False
	
linkedlist1=Node(5)
linkedlist1.next=Node(8)
linkedlist1.next=Node(4)
linkedlist1.next=Node(6)
linkedlist1.next=Node(7)
linkedlist1.next=Node(9)
linkedlist1.next=linkedlist1

linkedlist2=Node(5)
linkedlist2.next=Node(8)
linkedlist2.next=Node(4)
linkedlist2.next=Node(6)
linkedlist2.next=Node(7)
linkedlist2.next=Node(9)

print is_circular(linkedlist1)
print is_circular(linkedlist2)