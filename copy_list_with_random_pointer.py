"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        reference_map = {}
        ret = head
        while head != None:
            copy = Node(head.val, None, None)
            reference_map[head] = copy
            head = head.next
        #return reference_map[ret]
        new_start = ret
        # appending next and random
        while new_start != None:
            if new_start.next in reference_map:
                reference_map[new_start].next = reference_map[new_start.next]
            if new_start.random in reference_map:
                reference_map[new_start].random = reference_map[new_start.random]
            new_start = new_start.next
        return reference_map[ret]
