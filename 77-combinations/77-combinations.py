class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # nums=[i for i in range(1,n+1)]
        # print(nums)
        res=[]
        cur=[]
        def backtrack(pos,cur):
            if len(cur)==k:
                res.append(cur.copy())
                return
            for i in range(pos,n+1):
                cur.append(i)
                backtrack(i+1,cur)
                cur.pop()
        backtrack(1,cur)
        return res