class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum=0
        total_sum=nums[0]
        for i in range(len(nums)):
            if cur_sum<0:
                cur_sum=0
            cur_sum+=nums[i]
            total_sum=max(total_sum,cur_sum)
        return total_sum