class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(pos):
            if pos>=n:
                res.append(nums.copy())
                return
            for i in range(pos,n):
                nums[pos],nums[i]=nums[i],nums[pos]
                dfs(pos+1)
                nums[pos],nums[i]=nums[i],nums[pos]
        n=len(nums)
        dfs(0)
        return res
        