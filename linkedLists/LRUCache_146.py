class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode

    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        node.prev, node.next = prv, nxt
        prv.next = nxt.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

lRUCache = LRUCache(2)
lRUCache.put(2, 1) 
lRUCache.put(2, 2) 
assert(lRUCache.get(2) == 2)
lRUCache.put(1, 1) 
lRUCache.put(4,1)
assert(lRUCache.get(2) == -1)