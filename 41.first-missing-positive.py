#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        a = 1
        if nums[-1] < 0:
            return a
        for i in nums:
            if i == a:
                a += 1
        return a
# @lc code=end

