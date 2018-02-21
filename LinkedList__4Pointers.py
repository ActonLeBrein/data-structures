class Node:
    def __init__(self, data):
        self.data=data 
        self.left=None
        self.right=None
        self.up=None
        self.down=None

def node_search(data,node):
    if node is None:
        return False
    elif data==node.data:
        return True
    else:
        return (node_search(data,node.left) or 
                node_search(data,node.right) or
                node_search(data,node.up) or
                node_search(data,node.down))

def node_search_max1_max2(node,maxi=[0,-1]):
    if node is not None:
        if node.data>maxi[0]:
            maxi[0]=node.data
        elif node.data>maxi[1]:
            maxi[1]=node.data
        return (node_search_max1_max2(node.left,maxi),
                node_search_max1_max2(node.right,maxi),
                node_search_max1_max2(node.up,maxi),
                node_search_max1_max2(node.down,maxi))
    else:
        return maxi

root=Node(4)
root.left=Node(2)
root.right=Node(5)
root.up=Node(10)
root.down=Node(6)
root.left.up=Node(1)
root.right.down=Node(3)
root.up.right=Node(7)
root.down.left=Node(9)
print node_search(11,root)
print node_search_max1_max2(root)