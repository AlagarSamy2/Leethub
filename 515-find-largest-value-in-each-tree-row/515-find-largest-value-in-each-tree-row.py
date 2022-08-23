# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=[]
        cur=root
        q.append(cur)
        while q:
            level=[]
            for i in range(len(q)):
                temp=q.pop(0)
                if temp:
                    level.append(temp.val)
                    q.append(temp.left)
                    q.append(temp.right)
            if level:
                res.append(max(level))
        return res