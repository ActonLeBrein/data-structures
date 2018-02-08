class hashSet:
    def __init__(self, numSets):
        '''
       numBuckets: int. The number of buckets this hash set will have.
       Raises ValueError if this value is not an integer, or if it is not greater than zero.
 
       Sets up an empty hash set with numBuckets number of buckets.
       '''
        if type(numSets) != type(1) or numSets < 1:
            raise ValueError("")
 
        self.numSets = numSets
        self.sets = []
        self.succesadd = 0
        for i in range(numSets):
            self.sets.append([])
 
    def hashValue(self, e):
        '''
       e: an integer
 
       returns: a hash value for e, which is simply e modulo the number of
        buckets in this hash set. Raises ValueError if e is not an integer.
       '''
        if type(e) != type(1):
            raise ValueError("")        
        return e % self.numSets
       
    def member(self, e):
        '''
       e: an integer
       Returns True if e is in self, and False otherwise. Raises ValueError if e is not an integer.
       '''
        if type(e) != type(1):
            raise ValueError("")
               
        return e in self.sets[self.hashValue(e)]
 
    def insert(self, e):
        '''
       e: an integer
       Inserts e into the appropriate hash bucket. Raises ValueError if e is not an integer.
       '''
        if type(e) != type(1):
            raise ValueError("")
       
        if not self.member(e):
            self.succesadd +=1
            self.sets[self.hashValue(e)].append(e)
 
    def remove(self, e):
        '''
       e: is an integer
       Removes e from self
       Raises ValueError if e is not in self or if e is not an integer.
       '''
        if type(e) != type(1) or not self.member(e):
            raise ValueError("")
        else:
            self.sets[self.hashValue(e)].remove(e)
       
    def __str__(self):
        result = ""
        for i in range(self.numSets):
            result += "[" + str(i) + "] =>"
            result += str(self.sets[i]) + "\n"
        result += 'succesfull adds to hashset ' + str(self.succesadd) + ' '
        return result
 
    def getNumBuckets(self):
        return self.numSets

t = hashSet(6)
t.insert(5)
t.insert(79)
t.insert(5)
t.insert(576)
t.insert(79)
t.insert(50000)
t.insert(809)
t.insert(54243)
t.insert(200000)
print t
t.remove(5)
t.insert(032132)
print t
t.insert(5)
t.insert(67843874)
t.insert(678438)
t.insert(67874)
print t