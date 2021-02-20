/*
 * @lc app=leetcode.cn id=202 lang=javascript
 *
 * [202] 快乐数
 */
/**
 * @param {number} n
 * @return {boolean}
 */

// runtime: 98.83 % - memory - 52.76 %
var isHappy = function(n) {
    if (n == 1) {
        return true
    }
    memory = []
    memory.push(n)
    new_n = add(split(n))

    while (memory.indexOf(new_n) == -1 && new_n != 1) {
        memory.push(new_n)
        new_n = add(split(new_n))
    }
    return new_n == 1
};

function add(arr){
    let total = 0
    for (let value of arr){
        total += value * value
    }
    return total
}

function split(num){
    let arr = []
    while (num > 0) {
        arr.push(num % 10)
        num = Math.floor(num / 10)
    }
    return arr
}

// Others
// var _isHappy = function(n) {
//     let slow = n, fast = add(split(n))
//     while (slow != fast) {
//         slow = add(split(slow))
//         fast = add(split(fast))
//         fast = add(split(fast))
//     }
//     return slow == 1;
// };


