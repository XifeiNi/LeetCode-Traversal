# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        cols = collections.defaultdict(list)
        level= [(root,0)]
        while level:
            newlevel=[]
            level.sort(key = lambda x: x[0].val)
            for node, i in level:
                cols[i].append(node.val)
                if node.left:
                    newlevel.append((node.left,i-1))
                if node.right:
                    newlevel.append((node.right,i+1))
            level = newlevel
        return [cols[col] for col in sorted(cols)]
