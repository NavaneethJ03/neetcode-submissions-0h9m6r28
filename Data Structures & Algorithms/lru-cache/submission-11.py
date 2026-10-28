class Node:
    def __init__(self, key , val):
        self.key = key
        self.val = val 
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.left = Node(0 , 0)
        self.right = Node(0 , 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self , node):
        prvNode , nxtNode = node.prev , node.next
        prvNode.next = nxtNode 
        nxtNode.prev = prvNode
    
    def insert(self , node):
        prvNode = self.right.prev 
        prvNode.next , node.prev = node , prvNode 
        self.right.prev , node.next = node , self.right

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

        if len(self.cache) > self.size:
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)

