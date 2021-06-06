# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.count(root, root.val)
    def count(self, node, maximum):
        if not node:
            return 0
        mx = max(node.val, maximum)
        return 1 + self.count(node.left, mx) + self.count(node.right, mx) if node.val >= maximum else self.count(node.left, mx) + self.count(node.right, mx)
    
        