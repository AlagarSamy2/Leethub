class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visit=set()
        Row,Col=len(grid),len(grid[0])
        islands=0
        
        
        def bfs(r,c):
            q=[]
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col=q.pop(0)
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc  in directions:
                    r,c=row+dr,col+dc
                    if ( r in range(Row) and c in range(Col) and (r,c) not in visit and grid[r][c] =='1'):
                        q.append((r,c))
                        visit.add((r,c))
        for i in range(Row):
            for j in range(Col):
                if grid[i][j]=='1' and (i,j) not in visit: 
                    bfs(i,j)
                    islands+=1
        return islands