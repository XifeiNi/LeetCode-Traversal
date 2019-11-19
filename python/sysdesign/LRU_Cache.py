class Node:
    def __init__(self, key= None, value = None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

        
class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.hash = dict()
        self.head = Node(0,0) # dummy node
        self.tail = Node(0,0) # dummy node
        self.tail.prev = self.head
        self.head.next = self.tail


    def get(self, key):
        if key not in self.hash:
            return - 1

        node = self.hash[key]
        self._remove_node(node)
        self._move_to_tail(node)

        return node.value


    def put(self, key, value):
        if key in self.hash:
            self.hash[key].value = value # uddate value if value is changed
            node = self.hash[key]
            self._remove_node(node)
        else:
            if len(self.hash) == self.capacity:
                del self.hash[self.head.next.key]
                self.head.next = self.head.next.next
                self.head.next.prev = self.head

            node = Node(key, value)
            self.hash[key] = node

        self._move_to_tail(node)


    def _move_to_tail(self, node):
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next = node
        node.next = self.tail
        
        
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
