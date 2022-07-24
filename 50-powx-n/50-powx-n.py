class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1
        nn=n
        while nn!=0:
            if nn%2==0:
                x=x*x
                nn=int(nn/2)
            else:
                ans=x*ans
                nn=abs(nn)-1
        if n<0:
            return (1/ans)
        return ans