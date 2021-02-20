#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 81.24% 16.2%
class Solution:
    def rob(self, root: TreeNode) -> int:
        def max_node(node):
            if node is None:
                return (0, 0)
            left_max = max_node(node.left)
            right_max = max_node(node.right)
            max_with_self = left_max[1] + right_max[1] + node.val
            max_without_self = max(left_max) + max(right_max)
            return (max_with_self, max_without_self)
        return max(max_node(root))
    
        
# @lc code=end

