#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
from typing import List
# 7464 4574
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for p in prices:
            if p > min_price:
                new_profit = p - min_price
                if new_profit > max_profit:
                    max_profit = new_profit
            elif p < min_price:
                min_price = p
        return max_profit


# @lc code=end
