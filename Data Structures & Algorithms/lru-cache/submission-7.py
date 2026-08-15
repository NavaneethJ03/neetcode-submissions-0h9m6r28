class Node:
    def __init__(self , key , val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.cap = capacity
        self.left = Node(0 , 0)
        self.right = Node(0 , 0)
        self.left.next , self.right.prev = self.right , self.left

    def insert(self , node):
        prv = self.right.prev
        prv.next = node
        node.prev = prv 
        node.next = self.right
        self.right.prev = node

    def remove(self , node):
        prv = node.prev
        nxt = node.next
        prv.next = nxt
        nxt.prev = prv

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        self.remove(self.store[key])
        self.insert(self.store[key])
        return self.store[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.remove(self.store[key])
        node = Node(key , value)
        self.store[key] = node
        self.insert(node)
        if len(self.store) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.store[lru.key]
