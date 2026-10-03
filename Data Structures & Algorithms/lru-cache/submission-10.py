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
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self , node):
        prevNode = self.right.prev
        prevNode.next = node
        node.prev = prevNode
        node.next = self.right
        self.right.prev = node
    
    def remove(self, node):
        prevNode = node.prev 
        nextNode = node.next 
        prevNode.next = nextNode 
        nextNode.prev = prevNode 
        node.prev = node.next = None

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key , value)
        self.cache[key] = node
        self.insert(node)
        if len(self.cache) > self.cap:
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]
        
