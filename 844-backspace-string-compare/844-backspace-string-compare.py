class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1,stack2=[],[]
        for i in range(len(s)):
            if len(stack1)==0:
                if s[i]=='#':
                    continue
                else:
                    stack1.append(s[i])
                    continue
            if s[i]=='#':
                stack1.pop()
            else:
                stack1.append(s[i])
        for i in range(len(t)):
            if len(stack2)==0:
                if t[i]=='#':
                    continue
                else:
                    stack2.append(t[i])
                    continue
            if t[i]=='#':
                stack2.pop()
            else:
                stack2.append(t[i])
        if stack1==stack2:
                       return True
        return False
                       
                
            
            
            