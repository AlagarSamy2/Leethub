class Solution:
    def rob(self, nums: List[int]) -> int:
    
        def rob1(nums):
            dp=nums
            if len(nums)>=3:
                for i in range(len(nums)-3,-1,-1):
                    dp[i]=dp[i]+max(dp[i+2:])
            return max(dp)
        n=len(nums)
        if n<=2:
            return max(nums)
        max1=rob1(nums[:-1])
        max2=rob1(nums[1:])
        return(max(max1,max2))