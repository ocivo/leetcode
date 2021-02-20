#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List

# @lc code=start
# 1159 4566
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if (n < 3):
             return []
        nums.sort()
        ret = []
        for i in range(n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    ret.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1]:
                        left += 1
                        if left >= right:
                            break
                    continue
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return ret

# print(Solution().threeSum([-2,0,0,2,2]))
            


# @lc code=end

