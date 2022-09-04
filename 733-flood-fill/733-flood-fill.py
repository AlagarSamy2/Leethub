class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        Row=len(image)
        Col=len(image[0])
        source=image[sr][sc]
        def dfs(i,j):
            if (i<0 or i>=Row or j<0 or j>=Col):
                return
            elif (image[i][j]!=source):
                return
            image[i][j]=color
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        if (image[sr][sc]==color):
            return image
        dfs(sr,sc)
        return (image)
                
        