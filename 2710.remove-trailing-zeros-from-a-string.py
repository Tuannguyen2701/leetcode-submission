<<<<<<< HEAD
#
# @lc app=leetcode id=2710 lang=python3
#
# [2710] Remove Trailing Zeros From a String
#

# @lc code=start
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        while num[-1] == "0":
            num = num[:-1]
        return num
            
        
# @lc code=end

=======
#
# @lc app=leetcode id=2710 lang=python3
#
# [2710] Remove Trailing Zeros From a String
#

# @lc code=start
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        while num[-1] == "0":
            num = num[:-1]
        return num
            
        
# @lc code=end

>>>>>>> c948aa9344c66c8a60d3ad9f53b28a7453d3ad3b
