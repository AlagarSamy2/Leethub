class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count=0
        subarray=0
        total=0
        prod=1
        j=0
        for i in range(len(nums)):
            prod*=nums[i]
            subarray+=1
            while prod>=k and j<=i:
                prod=prod/nums[j]
                j+=1
                subarray-=1
            if prod<k:
                total+=subarray
        return total