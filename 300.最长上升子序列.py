#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#

# @lc code=start
# %14.62 5.43%
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        dp = [1]
        for num in nums[1:]:
            cur_max = 1
            for i, i_max in enumerate(dp):
                if nums[i] < num and i_max >= cur_max:
                    cur_max = i_max + 1
            dp.append(cur_max)
        return max(dp)
            
# @lc code=end

