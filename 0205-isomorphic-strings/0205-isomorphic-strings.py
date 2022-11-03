class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                if t[i] in list(d.values()):
                    return False
                else:
                    d[s[i]]=t[i]
            
            elif s[i] in d:
                if d[s[i]] != t[i]:
                    return False
        
        return True
        