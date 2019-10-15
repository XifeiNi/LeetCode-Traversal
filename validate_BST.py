# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root, -sys.maxsize, sys.maxsize)
    def dfs(self, root, small, large):
        if root is None:
            return True
        if root.val >= large or root.val <= small:
            return False
        return self.dfs(root.left, small, root.val) and self.dfs(root.right, root.val, large)
        
