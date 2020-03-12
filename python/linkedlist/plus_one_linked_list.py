# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
        if dummy.val == 1:
            return dummy
        else:
            return dummy.next
