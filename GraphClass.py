# Script text here
class Graph:
    def __init__(self):
        self.graph   = {}
        self.nodes   = []
        self.archval = {}
        
    def addnextnode(self, node, nextnode):
        temp = []
        temp = self.graph.get(node)
        if nextnode in temp:
            print "Ops! The NODE is already in the graph you BITCH!"
        elif self.graph.get(node):
            temp = self.graph.get(node)
            if nextnode in temp:
                self.graph[node] = temp
            else:
                temp = temp + [nextnode]
                self.graph[node] = temp
                self.graph[node].sort()
        else:
            self.graph[node] = [nextnode]
    
    def addnode(self, node):
        if not self.nodein(node):
            self.graph[node] = []
            self.nodes.append(node)
            self.nodes.sort()
        else:
            print "Ops! The NODE is already in the graph you BITCH!"
    
    def addarchval(self, node1, node2, val):
        if not self.nodein(node1):
            print "Ops! The NODE1 is not in the graph you BITCH!"
        elif not self.nodein(node2):
            print "Ops! The NODE2 is not in the graph you BITCH!"
        elif self.archin(node1 + node2):
            print "Ops! The ARCH is in the graph you BITCH!"
        elif val is None:
            print "Ops! The VALUE can not be null you BITCH!"
        else:
            self.archval[node1 + node2] = val
            self.archval[node2 + node1] = val
            self.addnextnode(node1, node2)
            self.addnextnode(node2, node1)
            
    def path(self, node1, node2):
        if node2 in self.graph.get(node1):
            return True
        else:
            return False
        
    def removearch(self, node1, node2):
        temp = []
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
            del self.graph[nod]
            self.nodes.remove(nod)
            while i < self.lengraph():
                temp2 = self.graph.get(self.nodes[i])
                if nod in temp2:
                    temp2.remove(nod)
                    self.graph[self.nodes[i]] = temp2
                    if self.archin(nod + self.nodes[i]):
                        self.removearch(nod, self.nodes[i])
                i += 1
        else:
            print "Ops! The NODE is not in the graph you BITCH!"
    
    def lengraph(self):
        return len(self.nodes)
    
    def nodein(self, node):
        if node in self.graph:
            return True
        else:
            return False
    
    def archin(self, node):
        if node in self.archval:
            return True
        else:
            return False
    
    def cleargraph(self):
        self.graph   = {}
        self.nodes   = []
        self.archval = {}
        
y = Graph()
y.addnode('A')
y.addnode('B')
y.addnode('C')
y.addnode('D')
y.addnode('E')
y.addnode('F')
y.addarchval('A','B',20)
y.addarchval('A','F',5)
y.addarchval('A','C',10)
y.addarchval('B','E',8)
y.addarchval('B','D',12)
y.addarchval('B','F',11)
y.addarchval('C','D',2)
y.addarchval('C','E',7)
y.addarchval('E','F',3)
print(y.graph)
print(y.archval)
print(y.nodes)
y.removenode('B')
print(y.graph)
print(y.archval)

w = Graph()
w.addnode('G')
w.addnode('J')
w.addnode('I')
w.addnode('H')
print(w.nodes)
w.addnextnode('G','J')
w.addnextnode('J','I')
w.addnextnode('I','G')
w.addnextnode('I','H')
w.addnextnode('H','G')
w.addnextnode('H','I')
print(w.graph)
w.removenode('G')
print(w.graph)

################################ NEW GRAPH CLASS ################################

# Script text here

class NewGraph:
    def __init__(self):
        self.graph = {}
        self.nodes = []
    
    def addnode(self, node1, node2, val):
        if val < 0:
            raise ValueError("")
        if node1 not in self.nodes:
            self.nodes.append(node1)
            self.nodes.sort()
        if node2 not in self.nodes:
            self.nodes.append(node2)
            self.nodes.sort()
        if self.graph.get(node1) is not None:
            self.graph[node1][node2] = val
        else:
            self.graph[node1] = {}
            self.graph[node1][node2] = val          
            
    def delete(self, node):
        if node not in self.nodes:
            raise ValueError("")
        else:
            i = 0
            self.nodes.remove(node)
            del self.graph[node]
            while i < len(self.nodes):
                if self.graph.get(self.nodes[i]) is None:
                    i += 1
                elif self.graph[self.nodes[i]].get(node) is None:
                    i += 1
                else:
                    del self.graph[self.nodes[i]][node]
                    i += 1
    
    def adjency(self, node):
        return self.graph[node].keys()
    
    def checkadj(self, node):
        if type(self.graph[node]) == type(1):
            return True
        else:
            return False

    def path(self, node1, node2):
        if self.graph[node1].get(node2):
            return True
        else:
            return False
        
    def value(self, node1, node2):
        if not self.path(node1,node2):
            raise ValueError("")
        else:
            return self.graph[node1][node2]
        
    def cleargraph(self):
        self.graph   = {}
        self.nodes   = []
        
        
def item(c,l):
    i = 0
    while i < len(l):
        if c == l[i][0]:
            break
        else:
            i += 1
    return i

def dijkstra(g,s):
    if g.checkadj(s):
        print "The node %s is not conntected to the other nodes in the graph" % s
    else:
        Q = g.nodes
        P = g.graph
        r = []
        S = []
        root = []
        j = 0
        for k in range(len(Q)):
            if s == Q[k]:
                i = s
                v = 0
                root = root + [[Q[k],0]]
                S = [s]
            else:
                r = r + [[Q[k],10000000]]
        c = []
        c = g.adjency(i)
        Q.remove(i)
        while len(r) > 1:
            while j < len(c):
                if g.value(i,c[j]) + v <= r[item(c[j],r)][1]:
                    r[item(c[j],r)][1] = g.value(i,c[j]) + v
                    j += 1
                else:
                    j += 1
            j = 0
            h = ['sos',100000000]
            while j < len(r):
                if r[j][1] <= h[1]:
                    h = r[j]
                    j += 1
                else:
                    j += 1
            j = 0
            root = root + [r.pop(item(h[0],r))]
            if h[0] in Q:
                Q.remove(h[0])
            S = S + [h[0]]
            v = h[1]
            i = h[0]
            c = []
            c = g.adjency(i)
        S = S + [Q[0]]
        root = root + [r[0]]
        print "The shortest path is: %s and its values are %s... BITCH IT WORKS XD!!!!" % (S, root)

y = NewGraph()
y.addnode('a','b',10)
y.addnode('a','c',3)
y.addnode('b','d',2)
y.addnode('b','c',1)
y.addnode('c','b',4)
y.addnode('c','d',8)
y.addnode('c','e',2)
y.addnode('d','e',7)
y.addnode('e','d',9)
print y.graph
print y.nodes
dijkstra(y,'a')
x = NewGraph()
x.addnode('a','b',7)
x.addnode('a','c',14)
x.addnode('a','d',9)
x.addnode('b','d',10)
x.addnode('b','e',15)
x.addnode('c','f',9)
x.addnode('d','c',2)
x.addnode('d','e',11)
x.addnode('e','f',6)
x.addnode('f','a',100)
print x.graph
print x.nodes
print dijkstra(x,'a')