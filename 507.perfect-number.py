<<<<<<< HEAD
#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        list = []
        for i in range(1,num):
            if num%i == 0:
                list.append(i)
        if sum(list) == num:
            return True
        else:
            return False
        
# @lc code=end

=======
#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        list = []
        for i in range(1,num):
            if num%i == 0:
                list.append(i)
        if sum(list) == num:
            return True
        else:
            return False
        
# @lc code=end

>>>>>>> c948aa9344c66c8a60d3ad9f53b28a7453d3ad3b
