#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        level = 0
        stack = [root] 
        while stack:
            level+= 1
            for x in range(len(stack)):
                node = stack.pop(0)
                if not node.left and not node.right: 
                    return level
                if node.left : 
                    stack.append(node. left)
                if node.right: 
                    stack.append(node.right)
        
# @lc code=end

