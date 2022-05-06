class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=list(s)
        t1=list(t)
        s1=sorted(s1)
        t1=sorted(t1)
        if s1==t1:
            return True
        else:
            return False
        