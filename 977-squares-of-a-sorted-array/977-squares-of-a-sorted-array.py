class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)):
            nums[i]=abs(nums[i])*abs(nums[i])
        nums=sorted(nums)
        return nums