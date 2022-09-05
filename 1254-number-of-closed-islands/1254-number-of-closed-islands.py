class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        Row=len(grid)
        Col=len(grid[0])
        count=0
        def dfs(i,j):
            if (i<0 or i>=Row or j<0 or j>=Col):
                return 0
            if grid[i][j]==1:
                return 1
            grid[i][j]=1
            a=dfs(i+1,j)
            b=dfs(i-1,j)
            c=dfs(i,j+1)
            d=dfs(i,j-1)
            return a and b and c and d
        for i in range(Row):
            for j in range(Col):
                if (grid[i][j]==0):
                    count=count+dfs(i,j)
        return (count)