class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=nums
        if len(dp)==1:
            return dp[-1]
        if len(dp)==2:
            return max(dp)
        for i in range(len(nums)-3,-1,-1):
            dp[i]=dp[i]+max(dp[i+2:])
        return max(dp)
            
        