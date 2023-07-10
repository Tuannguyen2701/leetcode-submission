#
# @lc app=leetcode id=908 lang=python3
#
# [908] Smallest Range I
#

# @lc code=start
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return 0
        else:
            return max(0,max(nums)-min(nums)-2*k)
        
# @lc code=end

