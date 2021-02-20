/*
 * @lc app=leetcode.cn id=7 lang=javascript
 *
 * [7] 整数反转
 */
/**
 * @param {number} x
 * @return {number}
 */
// runtime: 80.37% - memory - 46.74%
var reverse = function(x) {
    var sign = true;
    if (x === 0)
        return 0;
    else if (x < 0)
        sign = false;
    
    t = x.toString().split("").reverse().join("");
    start = 0;
    for (var i = 0; i < t.length; i++) {
        if (t.charAt(i) == "0"){
            start += 1;
        } else {
            break;
        }
    }
    t = t.substring(start);
    t = sign ? parseInt(t) : parseInt(t) * -1;
    if (t > Math.pow(2, 31) - 1 || t < -Math.pow(2, 31)) {
        return 0;
    } else {
        return t;
    }
    
};

