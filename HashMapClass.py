class HashMap:
    def __init__(self,size_strore):
        self.size_strore=size_strore
        self.store = [None for _ in range(size_strore)]
        self.size = 0

    def get(self, key):
        key_hash = self._hash(key)
        index = self._position(key_hash)
        if not self.store[index]:
            return None
        else:
            list_at_index = self.store[index]
            for i in list_at_index:
                if i.key == key:
                    return i.value
            return None

    def delete(self,key):
        key_hash = self._hash(key)
        index = self._position(key_hash)
        if not self.store[index]:
            return None
        else:
            self.store[index]=None
            return None

    def put(self, key, value):
        p = Node(key, value)
        key_hash = self._hash(key)
        index = self._position(key_hash)
        if not self.store[index]:
            self.store[index] = [p]
            self.size += 1
        else:
            list_at_index = self.store[index]
            if p not in list_at_index:
                list_at_index.append(p)
                self.size += 1
            else:
                for i in list_at_index:
                    if i == p:
                        i.value = p.value
                        return
                list_at_index.append(p)
                self.size += 1

    def __len__(self):
        return self.size

    def _hash(self, key):
        if isinstance(key, int):
            return key
        result = 5381
        for char in key:
            result = 33 * result + ord(char)
        return result

    def _position(self, key_hash):
        return key_hash % self.size_strore


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, other):
        return self.key == other.key


hashmap = HashMap(11)
hashmap.put(2, 12)
hashmap.put('asd', 13)
hashmap.put(0, 11)
print hashmap.store
print hashmap.get(0)
print hashmap.get('asd')
hashmap.delete('asd')
print hashmap.get('asd')
print hashmap.store