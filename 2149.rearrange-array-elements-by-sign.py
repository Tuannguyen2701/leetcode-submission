#
# @lc app=leetcode id=2149 lang=python3
#
# [2149] Rearrange Array Elements by Sign
#

# @lc code=start
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        list1 = []
        list2 = []
        x = []
        for i in nums:
            if i > 0:
                list1.append(i)
            else:
                list2.append(i)
        for i in range(len(list1)):
            x.append(list1[i])
            x.append(list2[i])
        return x
        
# @lc code=end

