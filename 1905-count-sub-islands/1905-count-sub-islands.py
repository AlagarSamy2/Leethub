class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        Row=len(grid1)
        Col=len(grid1[0])
        visit=set()
        def dfs(i,j):
            if (i<0 or i>=Row or j<0 or j>=Col or grid2[i][j]==0 or (i,j) in visit):
                return True
            res=True
            visit.add((i,j))
            if grid1[i][j]==0:
                res=False
            res=dfs(i+1,j) and res
            res=dfs(i-1,j) and res
            res=dfs(i,j+1) and res
            res=dfs(i,j-1) and res
            return res
        count=0
        for i in range(Row):
            for j in range(Col):
                if (grid2[i][j]==1 and (i,j) not in visit):
                    if dfs(i,j):
                        count+=1
        return (count)