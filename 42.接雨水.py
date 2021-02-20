#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# Time limit exceeded
# class Solution:
#     def trap(self, height):
#         if len(height) == 0:
#             return 0
#         reservoir = 0
#         size = len(height)
#         max_left = height[0]
#         for i in range(1, size):
#             max_left = max(max_left, height[i])
#             max_right = 0
#             for j in range(i, size):
#                 max_right = max(max_right, height[j])
#             reservoir += min(max_left, max_right) - height[i]
#         return reservoir

# runtime: 28.13% - memory - 5%
# class Solution:
#     def trap(self, height):
#         if len(height) < 3:
#             return 0
#         reservoir = 0
#         size = len(height)
#
#         max_left = height[0]
#
#         max_right_list = [None] * size
#         max_right_list[-1] = height[-1]
#
#         for i in range(size - 2, -1, -1):
#             max_right_list[i] = max(max_right_list[i + 1], height[i])
#
#         for i in range(1, size):
#             max_left = max(max_left, height[i])
#             reservoir += min(max_left, max_right_list[i]) - height[i]
#         return reservoir

# runtime: 42.57% - memory - 5%
class Solution:
    def trap(self, height):
        if len(height) < 3:
            return 0
        total = 0
        stack = []
        for current in range(len(height)):
            while len(stack) > 0 and height[current] > height[stack[-1]]:
                top = stack.pop(-1)
                if len(stack) == 0:
                    break
                distance = current - stack[-1] - 1
                bounded_height = min(height[current], height[stack[-1]]) - height[top]
                total += distance * bounded_height
            stack.append(current)
        return total
