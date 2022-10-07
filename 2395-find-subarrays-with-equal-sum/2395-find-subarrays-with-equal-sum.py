class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        dp=[]
        r=0
        for l in range(len(nums)-1):
            r=l+1
            if nums[l]+nums[r] in dp:
                return True
            dp.append(nums[l]+nums[r])
        return False