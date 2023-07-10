#
# @lc app=leetcode id=1287 lang=python3
#
# [1287] Element Appearing More Than 25% In Sorted Array
#

# @lc code=start
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        x = len(arr) // 4
        for i in set(arr):
            if arr.count(i) > x:    #Ktra số lần xuất hiện cua i có lớn hơn phần nguyên x 
                return i
        
# @lc code=end

