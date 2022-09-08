class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        Row,Col=len(heights),len(heights[0])
        pacific,atlantic=set(),set()
        
        def dfs(i,j,visit,prevHeight):
            if (i<0 or j<0 or i>=Row or j>=Col or heights[i][j]<prevHeight or (i,j) in visit):
                return
            visit.add((i,j))
            dfs(i-1,j,visit,heights[i][j])
            dfs(i+1,j,visit,heights[i][j])
            dfs(i,j-1,visit,heights[i][j])
            dfs(i,j+1,visit,heights[i][j])
        
        for c in range(Col):
            dfs(0,c,pacific,heights[0][c])
            dfs(Row-1,c,atlantic,heights[Row-1][c])
        
        for r in range(Row):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,Col-1,atlantic,heights[r][Col-1])
        res=[]
        for i in range(Row):
            for j in range(Col):
                if ((i,j) in pacific and (i,j) in atlantic):
                    res.append([i,j])
        return res