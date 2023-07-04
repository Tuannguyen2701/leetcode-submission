#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#

# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        x = 0
        for i in range(len(nums)-1):
            x = max(x, abs(nums[i] - nums[i+1]))
        return x            
        
# @lc code=end

