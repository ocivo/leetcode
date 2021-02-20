/*
 * @lc app=leetcode.cn id=46 lang=javascript
 *
 * [46] 全排列
 */
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
// runtime: 53.25 % - memory - 75.66 %
var permute = function(nums) {
    let results = []
    let step = function(exists, rests) {
        if (rests.length == 0) {
            results.push(exists)
        }
        for (let i = 0; i < rests.length; i++) {
            const next = rests[i]
            next_exists = exists.concat(next)
            next_rests = rests.slice(0, i).concat(rests.slice(i + 1))
            step(next_exists, next_rests)
        }
    }
    step([], nums)
    return results
};

