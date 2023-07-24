#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        h = heights
        n = len(h)
        m = len(h[0])
        isPac = [[True if i == 0 or j == 0 else False for j in range(m)] for i in range(n)]
        isAtl = [[True if i == n-1 or j == m-1 else False for j in range(m)] for i in range(n)]

        def Pac(i, j, isPac):
            val = h[i][j]
            for x,y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < n and 0 <= y < m and not isPac[x][y] and h[x][y] >=val:
                    isPac[x][y] = True
                    Pac(x, y, isPac)
        
        for i in range(n): Pac(i, 0, isPac)
        for j in range(m): Pac(0, j, isPac)
        for i in range(n): Pac(i, m-1, isAtl)
        for j in range(m): Pac(n-1, j, isAtl)
        
        return [[i,j] for i in range(n) for j in range(m) if isPac[i][j] and isAtl[i][j] ]
        
# @lc code=end

