class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(-1)
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self._get(index)

        return node.val if node is not None else -1
        
        
    def _get(self, index):

        node = self.head.next
        for i in range(index):
            if node is None:
                return -1
            node = node.next
        return node
    def _getPrev(self, index):
        if index == 0:
            return self.head
        node = self.head.next
        for i in range(index - 1):
            if node is None:
                return -1
            node = node.next
        return node
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        originalHead = self.head.next
        self.head.next = ListNode(val, originalHead)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node = self._getPrev(index)
        if node is not None:
            originalNext = node.next
            node.next = ListNode(val, originalNext)
        
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        node = self._getPrev(index)
        if node is not None and node.next is not None:
            node.next = node.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)