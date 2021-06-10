# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        res = ListNode(0)
        res.next = head
        start = res
        for _ in range(n):
            head = head.next
        while head != None:
            head = head.next
            start = start.next
        start.next = start.next.next
        return res.next