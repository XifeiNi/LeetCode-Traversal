# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.parse(nums, 0, len(nums) - 1)
    def parse(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right)//2
        root = TreeNode(nums[mid])
        root.left = self.parse(nums, left, mid - 1)
        root.right = self.parse(nums, mid + 1, right)
        return root
    
        
