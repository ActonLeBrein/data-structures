INT_MAX = 4294967296
INT_MIN = -4294967296
 
# A binary tree node
class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
 
def isBST(node):
    return (isBSTUtil(node, INT_MIN, INT_MAX))
 
def isBSTUtil(node, mini, maxi):
    if node is None:
        return True

    if node.data < mini or node.data > maxi:
        return False
 
    return (isBSTUtil(node.left, mini, node.data) and isBSTUtil(node.right, node.data, maxi))

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(10)
root.left.right = Node(3)
 
if (isBST(root)):
    print "Is BST"
else:
    print "Not a BST"