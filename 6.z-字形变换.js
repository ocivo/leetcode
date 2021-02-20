/*
 * @lc app=leetcode.cn id=6 lang=javascript
 *
 * [6] Z 字形变换
 */
/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
// runtime: 87.58% - memory - 40.91%
var convert = function(s, numRows) {
    if (numRows == 1) return s;

    var ret = "";
    var arrs = [];
    for (var i = 0; i < numRows; i++) {
        arrs.push([]);
    }

    var pointer = 0;
    for (var i = 0; i < s.length; i++) {
        arrs[pointer].push(s[i]);
        if (Math.floor(i / (numRows - 1)) % 2 == 0) {
            pointer += 1;
        } else {
            pointer -= 1;
        }
    }
    for (var i = 0; i < arrs.length; i++) {
        for (var j = 0; j < arrs[i].length; j++) {
            ret += arrs[i][j];
        }
    }

    return ret;

};

