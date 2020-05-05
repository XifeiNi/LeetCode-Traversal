# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        prev, cur = dummy, head
        while cur and cur.next:
            if cur.val == cur.next.val:
                value = cur.val
                while cur and cur.val == value:
                    cur = cur.next
                prev.next = cur
            else:
                cur = cur.next
                prev = prev.next
        return dummy.next
            
            
