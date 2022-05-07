class Solution:
    def firstUniqChar(self, s: str) -> int:
        s1={}
        for i in range(0,len(s)):
            if s[i] in s1:
                # print(i)
                s1[s[i]]+=1
            else:
                s1[s[i]]=1
        print(s1)
        for j in s1.keys():
            if s1[j]==1:
                print(s1[j])
                return s.index(j)
        return -1
                
        