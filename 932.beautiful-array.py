#
# @lc app=leetcode id=932 lang=python3
#
# [932] Beautiful Array
#

# @lc code=start
class Solution:
    def beautifulArray(self, n: int) -> List[int]:        
        ans = [1]
        while len(ans) < n:
            ans = [2*i - 1 for i in ans] + [2*i for i in ans]
        
        ans = [i for i in ans if i <= n]
        return ans 
        
# @lc code=end

