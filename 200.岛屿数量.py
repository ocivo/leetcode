#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
from typing import *
# @lc code=start
# 100% 86.9%
# 99.99% 88.97%
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        duplicates = {}
        counter = 0

        if grid[0][0] == "1":
            grid[0][0] = counter
            counter += 1
        for i in range(1, len(grid)):
            if grid[i][0] == "1":
                if grid[i - 1][0] != "0":
                    grid[i][0] = grid[i - 1][0]
                else:
                    grid[i][0] = counter
                    counter += 1
        for j in range(1, len(grid[0])):
            if grid[0][j] == "1":
                if grid[0][j - 1] != "0":
                    grid[0][j] = grid[0][j - 1]
                else:
                    grid[0][j] = counter
                    counter += 1
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                if grid[i][j] == "1":
                    pre_t = grid[i - 1][j]
                    pre_l = grid[i][j - 1]
                    if pre_t != "0" and pre_l == "0":
                        grid[i][j] = pre_t
                    elif pre_t == "0" and pre_l != "0":
                        grid[i][j] = pre_l
                    elif pre_t == "0" and pre_l == "0":
                        grid[i][j] = counter
                        counter += 1
                    elif pre_t == pre_l:
                        grid[i][j] = pre_t
                    else:
                        grid[i][j] = pre_t
                        set_t = duplicates.get(pre_t, set([pre_t]))
                        set_l = duplicates.get(pre_l, set([pre_l]))
                        
                        set_u = set_l.union(set_t)
                        for u in set_u:
                            duplicates[u] = set_u
            
        for d in set(map(tuple, duplicates.values())):
            counter -= (len(d) - 1)
        return counter

# @lc code=end
