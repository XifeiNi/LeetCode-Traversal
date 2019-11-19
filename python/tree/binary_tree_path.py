"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        if not root:
            return []
        # write your code here
        results = []
        self.dfs([], results, root)
        return results
    
    def dfs(self, path, results, node):
        path.append(str(node.val))
        if node.left is None and node.right is None:
            results.append('->'.join(path))
            path.pop()
            return
        if node.left:
            self.dfs(path, results, node.left)
            
        if node.right:
            self.dfs(path, results, node.right)
        path.pop()

