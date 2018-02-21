class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        tmp=self.items[-1]
        self.items=self.items[:-1]
        return tmp

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

class MinStack():
    def __init__(self):
        self.mini=None

    def mini_stack(self,stack):
        while stack.size()!=0:
            if self.mini is None:
                self.mini=stack.pop()
            elif self.mini>stack.peek():
                self.mini=stack.pop()
            else:
                stack.pop()
        return self.mini
        
s=Stack()
s.push(5)
s.push(8)
s.push(2)
s.push(3)
s.push(-1)
s.push(9)
print s.items
ms=MinStack()
print ms.mini_stack(s)