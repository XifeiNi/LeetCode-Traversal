# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0:
            return head
        listSize = self.getListSize(head)
        if listSize == 0:
            return head
        rotatedSize = k % listSize
        if listSize == 0 or rotatedSize == 0:
            return head

        originalTail = self.getCurrentListTail(head)
        
        k_node_prev = self.getKthNode(head, listSize - rotatedSize)
        k_node = k_node_prev.next
        k_node_prev.next = None
        
        
        self.connectHeadWithTail(head, originalTail)
        
        return k_node
        
    def getListSize(self, head):
        size = 0
        while head != None:
            head = head.next
            size+=1
        return size
    
    def getCurrentListTail(self, head):
        while head.next != None:
            head = head.next
        return head
    
    def connectHeadWithTail(self, head, tail):
        tail.next = head
    
    def getKthNode(self, head, k):
        for i in range(1, k):
            head = head.next
        return head
