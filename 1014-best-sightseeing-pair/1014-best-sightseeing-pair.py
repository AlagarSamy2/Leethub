class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans=0
        a=values[0]+0
        for i in range(1,len(values)):
            ans=max(ans,a+values[i]-i)
            a=max(a,values[i]+i)
        return ans