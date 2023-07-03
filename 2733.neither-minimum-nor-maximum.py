#
# @lc app=leetcode id=2733 lang=python3
#
# [2733] Neither Minimum nor Maximum
#

# @lc code=start
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        list1=[]
        q=deque()
        q.append(root)
        while q:
            level=[]
            for i in range(len(q)):
                poping=q.popleft()
                if poping:
                    level.append(poping.val)
                    q.append(poping.left)
                    q.append(poping.right)
            if level:
                list1.append(level)
        return list1
        
# @lc code=end

