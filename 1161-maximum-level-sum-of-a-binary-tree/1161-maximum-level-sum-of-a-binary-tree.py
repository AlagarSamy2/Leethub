# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q,res=[],[]
        cur=root
        q.append(cur)
        level_sum=0
        while q:
            level=[]
            for i in range(len(q)):
                temp=q.pop(0)
                if temp:
                    level.append(temp.val)
                    q.append(temp.left)
                    q.append(temp.right)
            if level:
                res.append(sum(level))
        max_sum=max(res)
        return res.index(max_sum)+1
            
            
        