#
# @lc app=leetcode id=888 lang=python3
#
# [888] Fair Candy Swap
#

# @lc code=start
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        x = (sum(aliceSizes)-sum(bobSizes)) / 2
        for i in bobSizes:
            if i + x in set(aliceSizes): 
                return [x + i, i]
        
# @lc code=end

