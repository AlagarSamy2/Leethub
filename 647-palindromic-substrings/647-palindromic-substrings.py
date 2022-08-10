class Solution:
    def countSubstrings(self, s: str) -> int:
        i=0
        count=0
        for i in range(len(s)):
            l=r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                count=count+1
                l-=1
                r+=1
            l=i
            r=l+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
        return count
            