class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp_heights=sorted(heights)
        count=0
        for i in range(0,len(heights)):
            if heights[i]!=exp_heights[i]:
                count+=1
        return count