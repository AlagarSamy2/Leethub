class Solution:
    def maximum69Number (self, num: int) -> int:
        num=list(str(num))
        for i in range(0,len(num)):
            if num[i]!='9':
                num[i]='9'
                break
        nums=[i for i in num]
        nums_s=''.join(nums)
        num=int(nums_s)
        print(num)
        return num