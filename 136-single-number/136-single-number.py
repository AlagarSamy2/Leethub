class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i], 0)+1
        for i in range(len(nums)):
            if d[nums[i]]==1:
                return nums[i]
        