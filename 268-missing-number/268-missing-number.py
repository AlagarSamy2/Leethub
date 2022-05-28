class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums,i=sorted(nums),0
        while True:
            try:
                if i!=nums[i]:
                    break
                i+=1
            except Exception:
                break
        return i
        