class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d={5:0,10:0,20:0}
        if bills[0]!=5:
            return False
        for i in range(len(bills)):
            d[bills[i]]=d.get(bills[i],0)+1
            if bills[i]!=5:
                if bills[i]==10:
                    if d[5]>0:
                        d[5]=d[5]-1
                    else:
                        return False
                elif bills[i]==20:
                    if d[10]>0 and d[5]>0:
                        d[10]=d[10]-1
                        d[5]=d[5]-1
                    elif d[5]>=3:
                        d[5]=d[5]-3
                    else:
                        return False
        return True
                
        