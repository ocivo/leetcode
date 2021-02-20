#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#

# @lc code=start
# 48.01% 18.54%
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = ""
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            sign = "-"
        numerator = abs(numerator)    
        denominator = abs(denominator)
        int_n = 0
        if numerator >= denominator:
            int_n = numerator // denominator
            numerator = numerator % denominator
        f_sec, duplicate_idx = self.calc_f_sec(numerator, denominator)
        if duplicate_idx != -1:
            f_sec = f_sec[:duplicate_idx] + "(" + f_sec[duplicate_idx:] + ")"
        if f_sec != "":
            f_sec = "." + f_sec 
        return sign + str(int_n) + f_sec

    def calc_f_sec(self, numerator, denominator):
        f_sec = ""
        nums = [numerator]
        numerator *= 10
        duplicate_idx = -1
        while numerator != 0:
            if numerator <= denominator:
                f_sec += "0"
            else:
                x = numerator // denominator
                numerator = numerator % denominator
                f_sec += str(x)
                if numerator in nums:
                    duplicate_idx = nums.index(numerator)
                    break
            nums.append(numerator)
            numerator *= 10
        return f_sec, duplicate_idx
      
# @lc code=end

# print(Solution().fractionToDecimal(-50, 8))
# print(Solution().fractionToDecimal(4, 55))
# print(Solution().fractionToDecimal(1, 6))
# print(Solution().fractionToDecimal(1, 2))
# print(Solution().fractionToDecimal(1, 4))
# print(Solution().fractionToDecimal(1, 16))
# print(Solution().fractionToDecimal(2, 2))
# print(Solution().fractionToDecimal(3, 2))
# print(Solution().fractionToDecimal(4, 2))
# print(Solution().fractionToDecimal(1, 3))
# print(Solution().fractionToDecimal(2, 3))
# print(Solution().fractionToDecimal(4, 333))
