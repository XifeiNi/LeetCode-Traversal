# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        self.depth = defaultdict(list)
        ans = []
        maxDepth = self.height(root)
        for i in range(1, maxDepth + 1):
            ans.append(self.depth[i])
        return ans
    def height(self, root):
        if root is None:
            return 0
        depth = max(self.height(root.left), self.height(root.right)) + 1
        self.depth[depth].append(root.val)
        return depth
