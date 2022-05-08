class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsindex={j:i for i,j in enumerate(nums1)}
        output=[-1]*len(nums1)
        
        stack=[]
        for i in range(len(nums2)):
            a=nums2[i]
            while stack and a>stack[-1]:
                val=stack.pop()
                idx=numsindex[val]
                output[idx]=a
            if a in nums1:
                stack.append(a)
        return output
        