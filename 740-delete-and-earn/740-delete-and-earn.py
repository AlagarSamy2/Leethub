class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d={}
        nums.sort()
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        nums=list(set(nums))
        dp=nums
        cur_value=0
        earn1,earn2=0,nums[0]*d[nums[0]]
        for i in range(1,len(nums)):
            cur_value=nums[i]*d[nums[i]]
            if nums[i]==nums[i-1]+1:
                temp=earn2
                earn2=max(earn2,cur_value+earn1)
                earn1=temp
            else:
                temp=earn2
                earn2=cur_value+earn2
                earn1=temp
        return earn2
                
                