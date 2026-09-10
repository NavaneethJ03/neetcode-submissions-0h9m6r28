class Node:
    def __init__(self, key , val):
        self.key = key 
        self.val = val
        self.next = self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0 , 0)
        self.right = Node(0 , 0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self , node):
        prv = self.right.prev 
        prv.next , node.prev = node , prv
        node.next , self.right.prev = self.right , node
    def remove(self , node):
        prv , nxt = node.prev , node.next
        prv.next = nxt
        nxt.prev = prv
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
            del self.cache[lru.key]
            self.remove(lru)
