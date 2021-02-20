#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 95.22% 5.03%
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_res = float("-inf")
        def go(node):
            nonlocal max_res
            if node is None:
                return
            go(node.left)
            go(node.right)
            left_val = 0 if node.left is None else node.left.val
            right_val = 0 if node.right is None else node.right.val
           
            max_left = max(0, left_val)
            max_right = max(0, right_val)

            max_res = max(max_res, node.val + max_left + max_right)
            node.val = max(max_left + node.val, max_right + node.val) 
        go(root)
        return max_res

# @lc code=end

