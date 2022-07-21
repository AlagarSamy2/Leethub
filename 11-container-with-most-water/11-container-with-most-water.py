class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        maxarea=0
        while l<r:
            temparea=abs(l-r) * min(height[l],height[r])
            maxarea=max(maxarea,temparea)
            if height[l]<height[r]:
                l=l+1
            elif height[r]<height[l]:
                r=r-1
            else:
                l=l+1
        return maxarea