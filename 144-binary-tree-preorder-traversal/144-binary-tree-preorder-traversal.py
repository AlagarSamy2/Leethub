# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        stack.append(root)
        res=[]
        while stack!=[]:
            temp=stack.pop()
            if temp:
                res.append(temp.val)
            else:
                break
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        return (res)
        # def dfs(cur):
        #     if not cur:
        #         return
        #     res.append(cur.val)
        #     dfs(cur.left)
        #     dfs(cur.right)
        # dfs(root)
        # return res