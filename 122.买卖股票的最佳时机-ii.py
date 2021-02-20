#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#
from collections import deque
from typing import List
# @lc code=start

# 7951 4677
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        if n < 2:
            return 0
        for i in range(1, n):
            if prices[i] >= prices[i - 1]:
                profit += prices[i] - prices[i - 1]
            
        return profit


# @lc code=end
