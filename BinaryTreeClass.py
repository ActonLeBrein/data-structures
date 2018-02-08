# Script text here
class BinaryTree:
    def __init__(self):
        self.tree   = []
        self.values = {}
        self.root   = None
    
    def getdad(self, node):
        i = 0
        c = None
        if self.nodein(node):
            while i < self.treelen():
                if node in self.tree[i]:
                    c = self.tree[i][0]
                else:
                    i += 1
    
    def leftchild(self, node):
        i = 0
        c = None
        while i < self.treelen():
            if node == self.tree[i][0]:
                if len(self.tree[i]) > 1:
                    c = self.tree[i][1]
                    break
                else:
                    break
            else:
                i += 1
        return c
    
    def rightchild(self, node):
        i = 0
        c = None
        while i < self.treelen():
            if node == self.tree[i][0]:
                if len(self.tree[i]) > 2:
                    c = self.tree[i][2]
                    break
                else:
                    break
            else:
                i += 1
        return c
    
    def addnode(self, node, val):
        c = None
        l = None
        r = None
        i = 0
        #Case 0: when tree is empty
        if val is not None and not self.nodein(node):
            if self.treelen() == 0:
                self.tree.append([node])
                self.nodeval(node) = val
                self.root = node
            else:
                while i < self.treelen():
                    #Case 1: val is less then father val
                    if self.nodeval(self.tree[i][0]) > val:
                        #Case 2: father doesn't have any childs, add left child
                        if self.haschilds(self.tree[i]) == 1:
                            self.tree[i] = self.tree[i] + [node]
                            self.values[node] = val
                            break
                        #Case 3: father has only 1 child, left child
                        elif self.haschilds(self.tree[i]) == 2:
                            c = self.nodeval(self.leftchild(self.tree[i][0]))
                            #Case 3.1: val is greater then left child value
                            if c < val:
                                self.tree[i] = self.tree[i] + [node]
                                self.values[node] = val
                                break
                            #Case 3.2: val is lesser then left child, goes to the left
                            else:
                                self.tree[i].insert(1,node)
                                self.values[node] = val
                                break
                        #Case 4: father has 2 childs, starts with left child
                        ###################### BEWARE ######################
                        l = self.nodeval(self.leftchild(self.tree[i][0]))
                        r = self.nodeval(self.rightchild(self.tree[i][0]))
                        #Case 5: val is greater then both childs, goes to right
                        #side it doesnt matter if right child has childs or not
                        elif l < val and r < val:
                            #Case 6: right child doesnt have childs or has 2 childs
                            if self.haschilds(self.rightchild(self.tree[i][0])) != 2:
                                self.tree[i][2] = node
                                self.tree.insert(i+1, [node, self.rightchild(self.tree[i][0])])
                                self.values[node] = val
                                break
                            #Case 7: right child has 1 child
                            else:
                                self.tree[i][2] = node
                                self.tree.insert(i, [node, self.leftchild(self.rightchild(self.tree[i][0])), self.rightchild(self.tree[i][0])])
                                self.values[node] = val
                                break
                        #Case 8: val is greater then left but less then right,
                        #goes to left side
                        elif l < val and r > val:
                            #Case 9: left child doesnt have childs or has 2 childs
                            if self.haschilds(self.leftchild(self.tree[i][0])) != 2:
                                self.tree[i][1] = node
                                self.tree.insert(i+1, [node, self.leftchild(self.tree[i][0])])
                                self.values[node] = val
                                break
                            else:
                                self.tree[i][1] = node
                                self.tree.insert(i, [node, self.leftchild(self.leftchild(self.tree[i][0])), self.leftchild(self.tree[i][0])])
                                self.values[node] = val
                                break
                        #Case 9: val is lesser then both childs, goes to the
                        #left side
                        else:
                            i += 1
                    #Case 6: val is greater then father then father becomnes
                    #left child and val becomes new tree root
                    else:
                        self.tree.insert(0,[node, self.tree[i][0]])
                        self.values[node] = val
                        self.root = node
                        break
        else:
            print "Ops! The NODE is already in the graph or value must be greater then zero you BITCH!"
            
    def haschilds(self, node):
        i = 0
        while i < self.treelen():
            if node == self.tree[i][0]:
                break
                return len(self.tree[i])
            else:
                i += 1
    
    def nodeval(self, node):
        return self.values[node]
#################    
    def deletenode(self, node):
    f = None
    l = None
    r = None
    i = 0
    if self.nodein(node):
        del self.values[node]
        #Case 0: node is root and len of tree is 1
        if node == self.root and self.treelen() == 1:
            self.cleartree()
        else:
            while i < self.treelen():
                if node == self.root:
                    
                elif node == self.tree[i][0]:
                    #Case 1: node doesnt have childs
                    if self.haschilds(node) == 1:
                        del self.tree[i]
                        break
                    #Case 2: node has 1 child
                    elif self.haschilds(node) == 2:
                        f = self.tree[i][0]
                        l = self.tree[i][1]
                        del self.tree[i]
                        break
                    else:?
#################    
            
        if self.graph.get(node1):
            temp = self.graph.get(node1)
            if node2 in temp:
                temp.remove(node2)
                self.graph[node1] = temp
        if self.graph.get(node2):
            temp = self.graph.get(node2)
            if node1 in temp:
                temp.remove(node1)
                self.graph[node2] = temp
        if self.archin(node1 + node2):
            del self.archval[node1 + node2]
            del self.archval[node2 + node1]
    
    def removenode(self, node):
        temp2 = []
        nod = node
        i = 0
        if self.nodein(node):
            print(self.graph.get(nod))
            del self.graph[nod]
            print(self.graph)
            self.nodes.remove(nod)
            print(self.nodes)
            while i < self.lengraph():
                temp2 = self.graph.get(self.nodes[i])
                if nod in temp2:
                    print "PASSED"
                    temp2.remove(nod)
                    self.graph[self.nodes[i]] = temp2
                    if self.archin(nod + self.nodes[i]):
                        self.removearch(nod, self.nodes[i])
                i += 1
        else:
            print "Ops! The NODE is not in the graph you BITCH!"
    
    def treelen(self):
        return len(self.tree)
    
    def nodein(self, node):
        if node in self.values:
            return True
        else:
            return False
    
    def cleartree(self):
        self.trees  = []
        self.values = {}
        self.root   = None
-----------------------------------------------------------------------
# Script text here
x = [['a','b','c'],['b','y','t'],['t','n','m'],['c','d','e'],['d','l','s'],['e','f','g'],['f','q','v'],['g','h','i'],['q','w','z'],['i','j','k'],['z','qq','yy']]
y = [['a', 'b', 'c'], ['c', 'd', 'e'], ['e', 'f', 'g'], ['g', 'h', 'i'], ['i', 'j', 'k']]
def move(t, n):
    c = n
    i = 0
    while i < len(t)-1:
        #Case 1: when node is root
        if t[i][0] == c and i == 0:
            #Case 2: when root doesn't have any children
            if len(t[i]) == 1:
                del t[i]
                break
            #Case 3: when root has only 1 child (left child always)
            elif len(t[i]) == 2:
                c = t[i][1]
                #Case 4: when left child has 2 children
                if len(t[i+1]) == 3:
                    t[i].append(t[i+1][2])
                    i += 1
                #Case 5: when left child has 1 child
                elif len(t[i+1]) == 2:
                    t[i].append(t[i+1][1])
                    i += 1
                #Case 6: when left child has no children
                else:
                    t[i].append(t[i+1][0])
                    i += 1
                del t[i][0]
            #Case 7: when root has 2 children (always bring the right child up)
            else:
                c = t[i][2]
                t[i][0] = t[i][2]
                del t[i][2]
                t[i].append(t[i+1][2])
                i += 1
        #Case 8: when node is a node at the end of the graph
        elif t[i][0] == c and i == len(t):
            #Case 9: when final node has no children
            if len(t[i]) == 1:
                del t[i]
                break
            #Case 10: when final node has 1 child
            elif len(t[i]) == 2:
                c = t[i][1]
                t[i-1][t[i-1].index(c)] = c
                '''if len(t[i+1]) == 3:
                    t[i].append(t[i+1][2])
                elif len(t[i+1]) == 2:
                    t[i].append(t[i+1][1])
                else:
                    t[i].append(t[i+1][0])
                del t[i]
                break'''
            #Case 11: when final node has 2 children
            else:
                c = t[i][2]
                t[i-1][t[i-1].index(c)] = c
                t[i][0] = t[i][2]
                break
        #Case 12: when node is equal to some node in graph
        elif t[i][0] == c:
            #Case 13: when node has no children
            if len(t[i]) == 1:
                del t[i]
                break
            #Case 14: when node has 1 child
            elif len(t[i]) == 2:
                c = t[i][1]
                t[i-1][t[i-1].index(c)] = c
                #Case 15: when node's child has 2 children
                if len(t[i+1]) == 3:
                    t[i].append(t[i+1][2])
                    i += 1
                #Case 16: when node's child has 1 child
                elif len(t[i+1]) == 2:
                    t[i].append(t[i+1][1])
                    i += 1
                
                else:
                    del t[i+1][0]
                    t[i].append(t[i+1][0])
                    i += 1
                del t[i][0]
            else:
                c = t[i][2]
                t[i-1][t[i-1].index(c)] = c
                t[i][0] = t[i][2]
                del t[i][2]
                t[i].append(t[i+1][2])
                i += 1
        else:
            i += 1
    t[i-1][2] = t[i][2]
    t[i][0] = t[i][2]
    del t[i][2]
    return t

#print 'x TREE'
#print x
#print move(x,'a')
print 'y TREE'
print y
print move(y,'a')
#print move(y,'k')