#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=list(str(x))
        b=list(str(x))
        b.reverse()
        if a == b:
            return True
        elif a != b:
            return False

                  
# @lc code=end

