# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        queue=[]
        queue.append(root)
        res=[]
        while queue:
            temp=queue.pop(0)
            if temp:
                res.append(temp.val)
                queue.append(temp.left)
                queue.append(temp.right)
        res.sort()
        l,r=0,len(res)-1
        while l<r and r<=len(res)-1 and l>=0:
            if res[l]+res[r]==k:
                return True
            elif res[l]+res[r]<k:
                l+=1
            else:
                r-=1
        return False