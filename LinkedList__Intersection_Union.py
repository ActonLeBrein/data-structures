class ListNode:
    def __init__(self,data):
        self.val=data
        self.next=None
        
class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def Intersection(self,headA,headB):
        curA,curB,curC=headA,headB,None
        while curA is not None:
            while curB is not None:
                if curA.val==curB.val:
                    newNode=ListNode(curA.val)
                    newNode.next=curC
                    curC=newNode
                    print 'Found a match'
                    break
                else:
                    curB=curB.next
            curA=curA.next
            curB=headB
            
        while curC is not None:
            print curC.val
            curC=curC.next

    def Union(self,headA,headB):
        curA,curB,curC,curC_head,flag=headA,headB,None,None,False
        while curA is not None:
            if curC_head is None:
                newNode=ListNode(curA.val)
                newNode.next=curC
                curC=newNode
                curC_head=curC
            else:
                while curC_head is not None:
                    if curA.val!=curC_head.val:
                        curC_head=curC_head.next
                    else:
                        flag=True
                        break
                if not flag:
                    newNode=ListNode(curA.val)
                    newNode.next=curC
                    curC=newNode
                    print 'Found a new item in listA {0}'.format(curA.val)
            flag=False
            curA=curA.next
            curC_head=curC
            
        while curB is not None:
            while curC_head is not None:
                if curB.val!=curC_head.val:
                    curC_head=curC_head.next
                else:
                    flag=True
                    break
            if not flag:
                newNode=ListNode(curB.val)
                newNode.next=curC
                curC=newNode
                print 'Found a new item in listB {0}'.format(curB.val)
            flag=False
            curB=curB.next
            curC_head=curC
            
        while curC is not None:
            print curC.val
            curC=curC.next
        
link_A=ListNode(2)
link_A.next=ListNode(5)
link_A.next.next=ListNode(10)
link_A.next.next.next=ListNode(4)

link_B=ListNode(1)
link_B.next=ListNode(5)
link_B.next.next=ListNode(1)
link_B.next.next.next=ListNode(10)
link_B.next.next.next.next=ListNode(105)
link_B.next.next.next.next.next=ListNode(2)

sol=Solution()
sol.Intersection(link_A,link_B)
sol.Union(link_A,link_B)