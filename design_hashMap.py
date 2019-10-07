class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap(object):

    def __init__(self, capacity=1001):
        """
        Initialize your data structure here.
        """
        self.capacity = capacity
        self.hashMap = [None] * capacity
        
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key % self.capacity
        node = self.hashMap[index]
        if node is None:
            self.hashMap[index] = ListNode(key, value)
            return
        pre = None
        while node:
            if node.key == key:
                node.val = value
                return
            pre = node
            node = node.next
        newNode = ListNode(key, value)
        pre.next = newNode


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.capacity
        node = self.hashMap[index]
        while node:
            #print(node.key)
            if node.key == key:
                return node.val
            node = node.next
        return -1
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        index = key % self.capacity
        node = self.hashMap[index]
        if node and node.key == key:
            self.hashMap[key % self.capacity] = node.next
            return
        pre = None
        while node:
            if node.key == key:
                pre.next = node.next
                return
            pre = node
            node = node.next
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
