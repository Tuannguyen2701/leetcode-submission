#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = list(itertools.permutations(nums))
        new_list = list(set(perm))
        return new_list
        
# @lc code=end

