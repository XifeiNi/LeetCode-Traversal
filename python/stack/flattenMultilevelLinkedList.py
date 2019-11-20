"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        curr, stack = head, []
        while curr:
            if curr.child is not None:
                if curr.next:
                    stack.append(curr.next)
                curr.next, curr.child.prev, curr.child = curr.child, curr, None
            else:
                if curr.next is None and len(stack) > 0:
                    temp = stack.pop()
                    temp.prev, curr.next = curr, temp
                curr = curr.next
        return head
