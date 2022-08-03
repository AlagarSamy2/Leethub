class Solution:
    def climbStairs(self, n: int) -> int:
        i,j=1,1
        while n>1:
            temp=j
            j=j+i
            i=temp
            n=n-1
        return j
        