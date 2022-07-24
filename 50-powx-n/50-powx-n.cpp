class Solution {
public:
    double myPow(double x, int n) {
        double  ans=1;
        int nn=n;
        while (nn!=0)
        {
            if (nn%2==0)
            {
                x=x*x;
                nn=nn/2;
            }
            else
            {
               ans=ans*x;
               nn=abs(nn)-1;
            }
    
        }
            if (n<0)
        {
            return (1/ans);
        }
        return ans;
};
};