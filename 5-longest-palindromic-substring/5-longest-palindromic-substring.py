class Solution:
    def longestPalindrome(self, s: str) -> str:
        l,r=0,0
        res=''
        reslen=0
        for i in range(0,len(s)):
            l=i
            r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>reslen:
                    res=s[l:r+1]
                    reslen=r-l+1
                l-=1
                r+=1
                # print(res)
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>reslen:
                    res=s[l:r+1]
                    reslen=r-l+1
                l-=1
                r+=1
                # print(res)
        return res
            
                
        