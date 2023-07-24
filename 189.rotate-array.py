#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        re = nums[-k:]
        re.extend(nums[:-k])
        for i in range(len(nums)): nums[i] = re[i]
           
        
# @lc code=end

