#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] 打乱数组
#
import random

# @lc code=start
# 73.72% 9.77%
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self._nums = [*nums]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = [*self._nums]
        return self.nums


    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.nums) - 1, -1, -1):
            swap_idx = random.randint(0, i)
            self.nums[i], self.nums[swap_idx] = self.nums[swap_idx], self.nums[i]
        return self.nums




# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

