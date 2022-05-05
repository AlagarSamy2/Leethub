class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        list1=[]
        list2=[]
        s1=list(s)
        print(s1)
        for i in range(0,len(s1)):
            if len(stack)==0:
                list1.append(i)
                stack.append(s1[i])
                continue
            if s1[i]=='(' and stack[0]==')':
                stack.pop()
                if len(stack)==0:
                    list1.append(i)
            if s1[i]==')' and stack[0]=='(':
                stack.pop()
                if len(stack)==0:
                    list1.append(i)
            else:
                stack.append(s1[i])
        if len(list1) ==0:
            return ""
        for j in range(0,len(s1)):
            if j not in list1:
                list2.append(s1[j])
        s2=''.join(str(a) for a in list2)
        return s2
                 