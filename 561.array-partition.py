#
# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition
#

# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        a = 0
        for i in range(0, len(nums), 2):
            a += min(nums[i], nums[i+1])
        return a
        
# @lc code=end

