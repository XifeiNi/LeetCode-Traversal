# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next and curr.next.next:
            tmp = curr.next.next
            curr.next.next = tmp.next
            tmp.next = curr.next
            curr.next = tmp
            curr = curr.next.next
        return dummy.next
