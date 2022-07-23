class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            v=nums[i]
            if v>= r-i:
                print("Changing")
                r=i
        if r==0:
            return True
        return False