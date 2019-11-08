"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        nodeMap = {}
        headPtr = head.next
        newNode = Node(head.val, None, None)
        nodeMap[head] = newNode
        newHead = newNode
        while headPtr != None:
            newNode.next = Node(headPtr.val, None, None)
            nodeMap[headPtr] = newNode.next
            headPtr = headPtr.next
            newNode = newNode.next
        retHead = newHead
        
        while retHead != None:
            if head.random is not None:
                retHead.random = nodeMap[head.random]
            retHead = retHead.next
            head = head.next
        return newHead
