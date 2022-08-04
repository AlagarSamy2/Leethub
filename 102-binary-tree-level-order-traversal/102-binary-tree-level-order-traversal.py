# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        queue=[]
        queue.append(root)
        while queue:
            level=[]
            queue_length=len(queue)
            for i in range(queue_length):
                temp=queue.pop(0)
                if temp:
                    level.append(temp.val)
                    queue.append(temp.left)
                    queue.append(temp.right)
            if level:
                res.append(level)
        return res
            