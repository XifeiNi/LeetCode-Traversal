"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        succ = None
        while root:
            if root.val >= p.val:
                root = root.left
            else:
                if succ == None or succ.val < root.val:
                    succ = root
                root = root.right
        return succ
