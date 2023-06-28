#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        for i in range(1, x+1):
            if i*i == x:
                return i
            elif i*i > x:
                return (i - 1)
# @lc code=end

