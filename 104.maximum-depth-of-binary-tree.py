#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        if root.right is None and root.left is None: return 1
        def maxDepth(root):
            if root is None: return 0
            if root.right is None and root.left is None: return 1
            return max(maxDepth(root.right), maxDepth(root.left)) +1
        return maxDepth(root) 
        
        
# @lc code=end

