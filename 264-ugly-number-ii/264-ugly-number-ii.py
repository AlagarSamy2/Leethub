class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp=[]
        dp.append(1)
        p2,p3,p5=0,0,0
        for i in range(1,n):
            mul2=dp[p2]*2
            mul3=dp[p3]*3
            mul5=dp[p5]*5
            dp.append(min(mul2,mul3,mul5))
            if dp[i]==mul2:
                p2+=1
            if dp[i]==mul3:
                p3+=1
            if dp[i]==mul5:
                p5+=1
        return dp[n-1]