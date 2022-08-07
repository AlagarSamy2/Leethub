class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        sum1=nums[0]*nums[1]*nums[-1]
        sum2=nums[-1]*nums[-2]*nums[-3]
        return max(sum1,sum2)