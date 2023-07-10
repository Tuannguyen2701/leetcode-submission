#
# @lc app=leetcode id=1492 lang=python3
#
# [1492] The kth Factor of n
#

# @lc code=start
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        list1 = []
        for i in range(1, n+1):
            if n%i == 0:
                list1.append(i)      
                if k <= len(list1):
                    return list1[k-1]
        return -1
                    
        
# @lc code=end

