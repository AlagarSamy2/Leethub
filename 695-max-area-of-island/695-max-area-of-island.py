class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Row=len(grid)
        Col=len(grid[0])
        visit=set()
        area1=0
        maxarea=0
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        def bfs(i,j):
            area=1
            q=[]
            q.append((i,j))
            visit.add((i,j))
            while q:
                r,c=q.pop()
                for dr,dc in directions:
                    row,col=r+dr,c+dc
                    if (row in range(Row) and col in range(Col) and grid[row][col]==1 and (row,col) not in visit):
                        area+=1
                        visit.add((row,col))
                        q.append((row,col))
            return area
        
        for i in range(Row):
            for j in range(Col):
                if (grid[i][j]==1 and (i,j) not in visit):
                    area1=bfs(i,j)
                    print(area1)
                    maxarea=max(maxarea,area1)
        return maxarea