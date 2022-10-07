class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        set1=set()
        r=0
        for l in range(len(nums)-1):
            r=l+1
            if nums[l]+nums[r] in set1:
                return True
            set1.add(nums[l]+nums[r])
        return False