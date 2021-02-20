#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#
# 32.23 %  5.06 %
class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        def swap(row, col):
            matrix[row][col], matrix[col][n - row - 1], matrix[n - row - 1][n - col - 1], matrix[n - col - 1][row] = \
            matrix[n - col - 1][row], matrix[row][col], matrix[col][n - row - 1], matrix[n - row - 1][n - col - 1]

        for row in range(n // 2):
            for col in range(row, n - row - 1):
                swap(row, col)

    def t(self, matrix):
        matrix[:] = map(list, zip(*matrix[::-1]))

# Others
# class Solution:
#     def rotate(self, matrix):
#         matrix[:] = map(list, zip(*matrix[::-1]))