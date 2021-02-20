/*
 * @lc app=leetcode.cn id=5 lang=javascript
 *
 * [5] 最长回文子串
 */
/**
 * @param {string} s
 * @return {string}
 */
// 77.98 %  65.09 %
var longestPalindrome = function(s) {
    if (s.length < 2){
        return s
    }
    function find1(i){
        left = i - 1
        right = i + 1
        length = 1
        while (left >= 0 && right <= s.length - 1){
            if (s[left] == s[right]) {
                left -= 1
                right += 1
                length += 2
            } else {
                break
            }
        }
        return s.substring(left+1, right)
    }

    function find2(i){
        if (i == 0 || s[i-1] != s[i]) {
            return s[i]
        }
        left = i - 1
        right = i
        length = 2
        while (left >= 0 && right <= s.length - 1){
            if (s[left] == s[right]) {
                left -= 1
                right += 1
                length += 2
            } else {
                break
            }
        }
        return s.substring(left+1, right)
    }

    max_str = s[0]
    for (let i = 0; i < s.length; i++) {
        current1 = find1(i)
        current2 = find2(i)
        if (current1.length > max_str.length) {
            max_str = current1
        }
        if (current2.length > max_str.length) {
            max_str = current2
        }
        
    }
    return max_str
};

