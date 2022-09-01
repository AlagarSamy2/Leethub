class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={0:1}
        res=0
        presum=0
        for i in range(len(nums)):
            presum+=nums[i]
            diff=presum-k
            if diff in d:
                res=res+d[diff]
            d[presum]=d.get(presum,0)+1
        return (res)