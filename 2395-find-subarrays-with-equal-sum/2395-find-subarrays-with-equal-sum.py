class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        dp=[]
        l,r=0,1
        while r<len(nums):
            if nums[l]+nums[r] in dp:
                return True
            dp.append(nums[l]+nums[r])
            l+=1
            r+=1
        return False