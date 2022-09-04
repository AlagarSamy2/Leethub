class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        Row=len(image)
        Col=len(image[0])
        sourceColour=image[sr][sc]
        def dfs(i,j):
            if (i<0 or i>=Row or j<0 or j>=Col):
                return
            elif (image[i][j]!=sourceColour):
                return
            image[i][j]=color
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in directions:
                row,col=i+dr,j+dc
                dfs(row,col)
        if image[sr][sc]==color:
            return image
        dfs(sr,sc)
        return (image)
        