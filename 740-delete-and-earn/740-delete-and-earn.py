class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        print(d)
        nums=sorted(list(set(nums)))
        earn1,earn2=0,0
        for i in range(len(nums)):
            cur_value=nums[i]*d[nums[i]]
            if i>0 and nums[i]==nums[i-1]+1:
                temp=earn2
                earn2=max(cur_value+earn1,earn2)
                earn1=temp
            else:
                temp=earn2
                earn2=cur_value+earn2
                earn1=temp
        return earn2
                