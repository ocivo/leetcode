#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
# 40.62 %  9.11 %
class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        outputs = []

        def backtrack(rests, exsists):
            if len(exsists) == len(nums):
                outputs.append(exsists)
                return

            for i in range(len(rests)):
                if i > 0 and rests[i] == rests[i - 1]:
                    continue
                backtrack(rests[:i] + rests[i+1:], exsists + [rests[i]])

        backtrack(nums, [])
        return outputs






        

