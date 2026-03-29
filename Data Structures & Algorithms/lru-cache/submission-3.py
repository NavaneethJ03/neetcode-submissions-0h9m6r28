class Node:
    def __init__(self , key , val):
        self.key = key
        self.val = val 
        self.next = None 
        self.prev = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity 
        self.left = Node(0 , 0) 
        self.right = Node(0 , 0)
        self.left.next = self.right 
        self.right.prev = self.left
        
    def remove(self , node):
        before , after = node.prev , node.next 
        before.next , after.prev = after  , before
    
    def insert(self , node):
        Previous = self.right.prev 
        Previous.next = node
        node.next = self.right
        node.prev = Previous
        self.right.prev = node
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key , value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
