class Node:
    def __init__(self,data,next=None):
        self.val=data
        self.next=next
    
    def getData(self):
        return self.val

    def setData(self,data):
        self.val=val

    def getNextNode(self):
        return self.next

class LinkedList:
    def __init__(self,head=None):
        self.head=head
        self.size=0

    def getSize(self):
        return self.size

    def contains(self,data):
        if self.head==None:
            return False
        else:
            tmp_head=self.head
            while tmp_head is not None:
                if tmp_head.val==data or data==None:
                    return True
                tmp_head=tmp_head.next
            return False
    
    def addNode(self,data):
        if not self.contains(data):
            newNode=Node(data,self.head)
            self.head=newNode
            self.size+=1
       
    def printNode(self):
        curr = self.head
        while curr:
            print curr.val
            curr = curr.next
     
class Solution:
    def Intersection(self,headA,headB):
        curA,curB,curC=headA.head,headB,LinkedList()
        while curA is not None:
            if curB.contains(curA.getData()):
                curC.addNode(curA.getData())
                print 'Found a match'
            curA=curA.getNextNode()
            
        curC.printNode()

    def Union(self,headA,headB):
        curA,curB,curC=headA.head,headB.head,LinkedList()
        while curA is not None:
            curC.addNode(curA.getData())
            curA=curA.getNextNode()
        while curB is not None:
            curC.addNode(curB.getData())
            curB=curB.getNextNode()
            
        curC.printNode()
        
link_A=LinkedList()
link_A.addNode(2)
link_A.addNode(5)
link_A.addNode(10)
link_A.addNode(4)
link_A.addNode(10)
print 'link_A '
link_A.printNode()

link_B=LinkedList()
link_B.addNode(5)
link_B.addNode(1)
link_B.addNode(10)
link_B.addNode(105)
link_B.addNode(2)
print 'link_B '
link_B.printNode()

sol=Solution()
print 'link_C intrsection '
sol.Intersection(link_A,link_B)
print 'link_C union '
sol.Union(link_A,link_B)
