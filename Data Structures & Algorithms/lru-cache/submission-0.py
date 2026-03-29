class Node:
    def __init__(self, val , key):
        self.val , self.key = val , key 
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left , self.right = Node(0 , 0) , Node(0 , 0)
        self.left.next , self.right.prev = self.right , self.left
        
    def remove(self , node):
        prevNode = node.prev if node.prev else None
        nextNode = node.next if node.next else None
        prevNode.next , nextNode.prev = nextNode , prevNode

    def insert(self , node):
        rightNodePrev = self.right.prev
        rightNodePrev.next = node 
        self.right.prev = node
        node.next = self.right
        node.prev = rightNodePrev
        


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(value , key)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
