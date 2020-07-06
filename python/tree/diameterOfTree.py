# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        _, diameter = self.longest(root)
        return diameter
        
    def longest(self, root):
        if not root:
            return 0, 0
        left, left_longest = self.longest(root.left)
        right, right_longest = self.longest(root.right)
        longest = max(left, right) + 1
        diameter = max(left_longest, right_longest, left + right )
        return longest, diameter
        
