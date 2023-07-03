<<<<<<< HEAD
#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        num = [True] * n
        if n > 0:
            num[0] = False
        if n > 1:
            num[1] = False
        for i in range(2, n):
            if num[i] == True:
                for j in range(i*i, n, i):
                    num[j] = False
        return num.count(True)
# @lc code=end

=======
#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        num = [True] * n
        if n > 0:
            num[0] = False
        if n > 1:
            num[1] = False
        for i in range(2, n):
            if num[i] == True:
                for j in range(i*i, n, i):
                    num[j] = False
        return num.count(True)
# @lc code=end

>>>>>>> c948aa9344c66c8a60d3ad9f53b28a7453d3ad3b
