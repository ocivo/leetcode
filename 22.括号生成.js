/*
 * @lc app=leetcode.cn id=22 lang=javascript
 *
 * [22] 括号生成
 */
/**
 * @param {number} n
 * @return {string[]}
 */

// runtime: 90.17 % - memory - 62.95 %
var generateParenthesis = function(n) {
    if (n == 0) {
        return []
    }
    let left = n;
    let right = n;
    let total = [];
    function step(str, cur_left, cur_right) {
        if (cur_left == 0 && cur_right == 0) {
            total.push(str);
        } else if (cur_left == cur_right) {
            str += "(";
            step(str, cur_left - 1, cur_right);
        } else if (cur_left == 0) {
            str += ")";
            step(str, cur_left, cur_right - 1);
        } else if (cur_left < cur_right) {
            str1 = str + "(";
            step(str1, cur_left - 1, cur_right);
            str2 = str + ")";
            step(str2, cur_left, cur_right - 1);
        }
    }
    step("", left, right);
    return total
};
