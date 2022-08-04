# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        queue=[]
        queue.append(root)
        while queue:
            qlen=len(queue)
            level=[]
            rightNode=None
            for i in range(qlen):
                temp=queue.pop(0)
                if temp:
                    rightNode=temp
                    queue.append(temp.left)
                    queue.append(temp.right)
            if rightNode:
                res.append(rightNode.val)
        return res