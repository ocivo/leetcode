import java.util.ArrayList;

/*
 * @lc app=leetcode.cn id=9 lang=java
 *
 * [9] 回文数
 */
// runtime: 25.06% - memory - 84.83%
class Solution {
    ArrayList<Integer> lst = new ArrayList<Integer>();

    public boolean isPalindrome(int x) {
        if (x < 0)
            return false;
        recursive(x);
        for (int i = 0; i < lst.size(); i++) {
            if (i >= lst.size() / 2) {
                break;
            }
            int left = lst.get(i);
            int right = lst.get(lst.size() - 1 - i);
            if (left != right) {
                return false;
            }
        }
        return true;
    }

    public void recursive(int x) {  
        if (x == 0) {
            return;
        }
        int x1 = x % 10;
        int x2 = x / 10;
        lst.add(x1);
        recursive(x2);
    }
}

