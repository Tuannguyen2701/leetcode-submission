#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            j = i-1
            count = 0
            while j >= 0:
                if nums[i] > nums[j]:
                    count += 1
                j -= 1
            k = i + 1
            while k < len(nums):
                if nums[i] > nums[k]:
                    count += 1
                k += 1
            result.append(count)
        return result
        
        
# @lc code=end

