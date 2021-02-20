#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# runtime: 19.69% - memory - 96.76%
# class Solution:
#     def twoSum(self, nums, target):
#         for i, num in enumerate(nums):
#             next = target - num
#             for j, _next in enumerate(nums[i+1:]):
#                 if _next == next:
#                     return [i, i + j + 1]
#         return []

# runtime: 52.5% - memory - 5.29%
class Solution:
    def twoSum(self, nums, target):
        _dict = {}
        for i, num in enumerate(nums):
            _dict[num] = i
        for j, num in enumerate(nums):
            next = target - num
            if next in _dict and _dict[next] != j:
                return [_dict[next], j]
        return []


