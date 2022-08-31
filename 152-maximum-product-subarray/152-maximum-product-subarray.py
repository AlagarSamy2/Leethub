class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=max(nums)#because if we have one number [-1] we need output as -1 not as 0
        max_prod=1
        min_prod=1
        for i in range(len(nums)):
            if nums[i]==0:
                max_prod,min_prod=1,1
                continue
            temp=max_prod#in min_prod calc we need old max_prod
            max_prod=max(nums[i]*max_prod,nums[i]*min_prod,nums[i])
            min_prod=min(nums[i]*temp,nums[i]*min_prod,nums[i])
            print(max_prod,min_prod)
            ans=max(max_prod,ans)
        return ans
           