#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#

# @lc code=start
# 20.15% 5.11%
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        if len(self.nums) == 0:
            self.nums.append(num)
        else:
            self.insert(0, len(self.nums), num)
        
    def insert(self, start, end, num):
        if end - start <= 1:
            if self.nums[start] >= num:
                self.nums.insert(start, num)
            else:
                self.nums.insert(start+1, num)
            return

        mid = (end - 1 - start) // 2 + start
        # print(end, start, mid, len(self.nums), num)
        if self.nums[mid] > num:
            # print("here")
            self.insert(start, mid, num)
        elif self.nums[mid] < num:
            self.insert(mid+1, end, num)
        else:
            self.nums.insert(mid, num)

    def findMedian(self) -> float:
        if len(self.nums) % 2 == 0:
            mid = len(self.nums) // 2
            return (self.nums[mid-1] + self.nums[mid]) / 2
        else:
            return self.nums[len(self.nums) // 2]
# mf = MedianFinder()     
# mf.addNum(-1)
# mf.addNum(-2)
# mf.findMedian()
# mf.addNum(-3) 
# mf.findMedian()
# mf.addNum(-4) 
# mf.addNum(-5) 

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

