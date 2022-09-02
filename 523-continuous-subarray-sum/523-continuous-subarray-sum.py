class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum=0
        d={0:-1}
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            rem=prefix_sum%k
            if rem not in d:
                d[rem]=i
            elif i-d[rem]>1:
                return True
        return False