class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        nums=sorted(set(nums))
        dp=[1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            # print(nums[i]-nums[i+1]) 
            if nums[i]-nums[i+1]==-1:
                dp[i]=dp[i]+dp[i+1]
        return max(dp)