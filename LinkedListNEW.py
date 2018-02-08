class node:
    def __init__(self):
        self.data = None
        self.next = None
        
class linklist:
    def __init__(self):
        self.first_node = None
        self.current_node = None
        
    def add_node_insert(self,data):
        if self.first_node is None:
            new_node = node()
            new_node.data = data
            new_node.next = self.current_node
            self.first_node = new_node
            self.current_node = new_node
        else:
            new_node = node()
            new_node.data = data
            new_node.next = self.current_node
            self.current_node = new_node
     
    def add_node_append(self,data):
        if self.current_node:
            while self.current_node.next != None:
                self.current_node = self.current_node.next
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.current_node.next = new_node
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.first_node = new_node
        self.current_node =  self.first_node

    def delete(self, data):
        previous = None
        found = False
        while self.current_node and found is False:
            if self.current_node.data == data:
                found = True
            else:
                previous = self.current_node
            	self.current_node = self.current_node.next
        if self.current_node is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
    else:
        previous.set_next(current.get_next())