class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for i in range(0,len(s)):
            if len(stack)==0:
                stack.append(s[i])
                continue
            if stack[-1].isupper():
                if stack[-1].lower()==s[i]:
                    stack.pop()
                else:
                    stack.append(s[i])
            elif stack[-1].islower():
                if stack[-1].upper()==s[i]:
                    stack.pop()
                else:
                    stack.append(s[i])
        stack=''.join(stack)
        # print(stack)
        return stack
            
            
            
        