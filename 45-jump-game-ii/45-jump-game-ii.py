class Solution:
    def jump(self, nums: List[int]) -> int:
        ptr = len(nums)-1
        count=0
        while ptr!=0:
            for i in range(0,ptr):
                if nums[i]>= ptr-i:
                    ptr=i
                    count+=1
                    # print(count)
                    break
            
        return count