class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
class DataStream:

    def __init__(self):
        self.head = Node() # dummy Node
        self.tail = self.head
        self.hash = {}
        self.used = set()
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        if num in self.used:
	    if num not in self.hash:
r		return
            self.remove(self.hash[num])
        else:
            self.used.add(num)
            self.tail.next = Node(num, self.tail, None)
            self.tail = self.tail.next
            self.hash[num] = self.tail
            
        
    def remove(self, node):
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.tail:
            node.tail = node.tail.prev
        node.prev, node.next = None, None
        del self.hash[node.value]
        

    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        if not self.head.next:
            return -1
        return self.head.next.value

data = DataStream()
data.add(1)
data.add(2)
print(data.firstUnique())
data.add(1)
print(data.firstUnique())
# On branch master
# Your branch is up to date with 'origin/master'.
#
# Changes to be committed:
#	new file:   657_insert_delete_getRandom.py
#
