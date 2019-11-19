# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummyNode = ListNode(-1)
        dummyNode.next = head
        mth_prev = self.findKthElement(dummyNode, m - 1)
        mth = mth_prev.next
        nth = self.findKthElement(dummyNode, n)
        nth_next = nth.next
        nth.next = None
        
        self.reverse(mth)
        
        mth_prev.next = nth
        mth.next = nth_next
        
        return dummyNode.next
        
    def findKthElement(self, head, k):
        for i in range(k):
            if head is None:
                return None
            head = head.next
        return head
    def reverse(self, head):
        prev = None
        while head!= None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
    
