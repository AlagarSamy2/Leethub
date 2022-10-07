class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        target=sum(nums)//2
        set1=set()
        set1.add(0)
        for i in range(len(nums)-1,-1,-1):
            set2=set()
            for j in set1:
                set2.add(j)
                set2.add(j+nums[i])
            if target in set2:
                return True
            for k in set2:
                set1.add(k)
        return False