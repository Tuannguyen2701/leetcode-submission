#
# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        x = len(nums)
        nums.sort()
        for i in nums:
          a = nums[x-1] * nums[x-2] * nums[x-3]
          b = nums[x-1] * nums[0] * nums[1]
        return max(a,b)
        
# @lc code=end

