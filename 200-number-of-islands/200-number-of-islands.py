class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Row=len(grid)
        Col=len(grid[0])
        visitSet=set()
        islands=0
        def bfs(i,j):
            q=[]
            visitSet.add((i,j))
            q.append((i,j))
            while q:
                r,c=q.pop(0)
                directions=[[-1,0],[1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    row,col=r+dr,c+dc
                    if (row in range(Row) and col in range(Col) and (row,col) not in visitSet and grid[row][col]=='1'):
                        visitSet.add((row,col))
                        q.append((row,col))
        for i in range(Row):
            for j in range(Col):
                if (grid[i][j]=='1' and (i,j) not in visitSet):
                    bfs(i,j)
                    islands+=1
        return islands
        