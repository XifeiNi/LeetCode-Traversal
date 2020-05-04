# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        left, right = dummy, dummy
        while right.next != None:
            right = right.next
            if right.val != 9:
                left = right
            
        if right.val != 9:
            right.val += 1
        else:
            left.val += 1
            left = left.next
            while left != None:
                left.val = 0
                left = left.next
        if dummy.val == 0:
            return dummy.next
        else:
            return dummy
        
