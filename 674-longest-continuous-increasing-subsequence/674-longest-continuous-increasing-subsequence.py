class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count=[1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                count[i]=max(count[i],count[i]+count[i+1])
        return max(count)
        