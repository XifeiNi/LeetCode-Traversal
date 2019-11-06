# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        left = True
        ret = []
        queue = deque([root])
        while queue:
            sub = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                sub.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            if not left:
                sub = sub[::-1]
            left = not left
            ret.append(sub)
        return ret
                    
