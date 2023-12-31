#
# @lc app=leetcode id=1848 lang=python3
#
# [1848] Minimum Distance to the Target Element
#

# @lc code=start
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        a = inf
        for i,j in enumerate(nums):
            if j == target:
                a = min(a,abs(i - start))
        return a
        
# @lc code=end

