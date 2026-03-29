class Node:
    def __init__(self, key: int, val: int, next: Optional['Node'] = None, prev: Optional['Node'] = None):
        self.val=val
        self.key=key
        self.next= None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(-1, -1)        
        self.tail = self.head
    def printLL(self):
        print("###################")
        curr = self.head
        while curr:
            print('----------')
            print(f'val: {curr.val}')
            if curr.prev:
                print(f'prev: {curr.prev.val}')
            if curr.next:
                print(f'next: {curr.next.val}')
            curr = curr.next
    def add(self, node: Node):
        # add node to tail of LL
        node.next = None
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
    def remove(self, node: Node):
        nextNode = node.next
        prevNode = node.prev
        prevNode.next = nextNode
        if nextNode:
            nextNode.prev = prevNode
        else:
            self.tail = prevNode
        node.next=None
        node.prev= None
        return node.key
    def get(self, key: int) -> int:
        if key in self.cache:
            oldNode = self.cache[key]
            self.remove(oldNode)
            self.add(oldNode)
            return oldNode.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add(node)
            return 
        if len(self.cache) < self.capacity:
            newNode = Node(key=key, val=value)
            self.cache[key] = newNode
            self.add(newNode)
            return
        
        removeKey = self.remove(self.head.next)
        del self.cache[removeKey]
        newNode = Node(key=key, val=value) 
        self.cache[key] = newNode
        self.add(newNode)
        return 