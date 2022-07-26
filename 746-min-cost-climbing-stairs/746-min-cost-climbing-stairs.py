class Solution:
    def minCostClimbingStairs(self, nums: List[int]) -> int:
        nums.append(0)
        for i in range(len(nums)-3,-1,-1):
            nums[i]=min(nums[i]+nums[i+1],nums[i]+nums[i+2])
        return min(nums[0],nums[1])
        