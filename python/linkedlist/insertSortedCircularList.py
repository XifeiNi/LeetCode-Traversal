"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head == None:
            head =  Node(insertVal)
            head.next = head
            return head
        insert = False
        prev, curr = head, head.next
        while True:
            if prev.val <= insertVal <= curr.val:
                insert = True
            if prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    insert = True
            if insert:
                prev.next = Node(insertVal, curr)
                return head
            prev, curr = curr, curr.next
            if prev == head:
                break
        prev.next = Node(insertVal, curr)
        return head
