# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum1, sum2 = 0, 0
        while l1:
            sum1 = sum1*10 + l1.val
            l1 = l1.next
        while l2:
            sum2 = sum2*10 + l2.val
            l2 = l2.next
        res = str(sum1 + sum2)
        dummy = ListNode(-1)
        head = dummy
        for i in range(len(res)):
            value = int(res[i])
            dummy.next = ListNode(value)
            dummy = dummy.next
        return head.next
        
