class Solution:
    def climbStairs(self, n: int) -> int:
        one,two=1,1
        temp=0
        total=0
        n=n-2
        while n>=0:
            total=one+two
            one,two=total,one
            n-=1
        return one 
    
        