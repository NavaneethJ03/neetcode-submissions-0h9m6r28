class Node:
    def __init__(self , key , val):
        self.key = key 
        self.val = val 
        self.next = self.prev = None 
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity 
        self.left , self.right = Node(0,0) , Node(0 , 0)
        self.left.next = self.right 
        self.right.prev = self.left

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

    def insert(self , node):
        previous = self.right.prev
        previous.next = node 
        node.prev = previous 
        node.next = self.right
        self.right.prev = node

    def remove(self , node):
        previous = node.prev 
        nextNode = node.next 
        previous.next = nextNode 
        nextNode.prev = previous
