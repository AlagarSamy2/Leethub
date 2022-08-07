class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_sum=0
        total_sum=nums[0]
        for i in nums:
            if cur_sum>0:
                cur_sum=0
            cur_sum+=i
            total_sum=min(total_sum,cur_sum)
        min_sum=sum(nums)-total_sum
        cur_sum=0
        total_sum=nums[0]
        for i in nums:
            if cur_sum<0:
                cur_sum=0
            cur_sum+=i
            total_sum=max(total_sum,cur_sum)
        if min_sum==0:
            return total_sum
        return max(total_sum,min_sum)