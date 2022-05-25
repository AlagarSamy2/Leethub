class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(0,len(image)):
            print(image[i])
            image[i]=image[i][::-1]
            # print(image[i],'Reversed')
            for j in range(0,len(image)):
                image[i][j]=abs(image[i][j]-1)
        return image
        