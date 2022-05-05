class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for i in range(0,len(s)):
            if len(stack)==0:
                stack.append(s[i])
                continue
            if s[i]==stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        print(stack)
        s=''.join(str(e) for e in stack)
        return s
        