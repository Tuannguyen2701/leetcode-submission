#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        out = []
        for i in nums:
            if nums.count(i) == 1:
                out.append(i)
        return out
        
# @lc code=end

