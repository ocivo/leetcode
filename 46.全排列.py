#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# 99.81 % 5.27 %
from itertools import permutations
class Solution:
    def permute(self, nums):
        return list(map(list, permutations(nums)))