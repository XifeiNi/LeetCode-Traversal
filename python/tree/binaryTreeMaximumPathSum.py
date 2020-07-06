# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxVal, _ = self._maxPathSum(root)
        return maxVal
    def _maxPathSum(self, root):
        if root is None:
            return -10000000, 0
        leftMax, leftSingle = self._maxPathSum(root.left)
        rightMax, rightSingle = self._maxPathSum(root.right)
        pathMax = max(leftMax, rightMax, root.val + leftSingle + rightSingle)
        single = max(leftSingle + root.val, rightSingle + root.val, 0)
        return pathMax, single
