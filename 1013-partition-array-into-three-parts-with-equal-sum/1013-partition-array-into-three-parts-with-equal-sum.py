class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        count=0
        target=sum(arr)//3
        if sum(arr)%3!=0:
            return False
        prefix_sum=0
        for i in range(len(arr)):
            prefix_sum=prefix_sum+arr[i]
            if prefix_sum==target:
                count+=1
                prefix_sum=0
        print(count)
        return count>=3