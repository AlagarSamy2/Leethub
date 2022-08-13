class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        Row,Col=len(grid),len(grid[0])
        visit=set()
        def dfs(i,j):
            # perm=0
            if i<0 or j<0 or i>=Row or j>=Col or grid[i][j]==0:
                return 1
            if (i,j) in visit:
                return 0
            visit.add((i,j))
            perm=dfs(i,j+1)
            perm=perm+dfs(i,j-1)
            perm=perm+dfs(i+1,j)
            perm=perm+dfs(i-1,j)
            return perm
        for i in range(Row):
            for j in range(Col):
                if grid[i][j]==1:
                    return dfs(i,j)
                    
        # return perm