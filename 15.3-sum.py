#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        tripnums = set()
        for i in range(len(nums) - 2):
            firstNum = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                secondNum  = nums[j]
                thirdNum = nums[k]

                potentialSum = firstNum + secondNum + thirdNum 
                if potentialSum > 0:
                    k -= 1
                elif potentialSum < 0:
                    j += 1
                else:
                    tripnums.add((firstNum , secondNum ,thirdNum))
                    j += 1
                    k -= 1
        return tripnums
        
# @lc code=end

