/*
 * @lc app=leetcode.cn id=11 lang=java
 *
 * [11] 盛最多水的容器
 */
// runtime: 99.1% - memory - 94.14%
class Solution {
    public int maxArea(int[] height) {
        int i = 0;
        int j = height.length - 1;
        int max = 0;
        while (i != j) {
            int area = calArea(i, height[i], j, height[j]);
            if (area > max) {
                max = area;
            }

            if (height[i] > height[j]) {
                j -= 1;
            } else {
                i += 1;
            }
        }

        return max;
    }

    public int calArea(int x1, int y1, int x2, int y2) {
        int h = y2 - y1 >= 0 ? y1 : y2;
        return (x2 - x1) * h;
    }
}

