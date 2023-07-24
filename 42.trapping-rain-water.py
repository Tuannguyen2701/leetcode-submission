#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        re = 0
        l = 0
        r = len(h) - 1
        m_l = h[l]
        m_r = h[r]
        while l < r:
            if m_l <= m_r:
                l += 1
                m_l = max(m_l, h[l])
                re += m_l - h[l]
            else:
                r -= 1
                m_r = max(m_r, h[r])
                re += m_r - h[r]
            print(re)
        return re
        
# @lc code=end

