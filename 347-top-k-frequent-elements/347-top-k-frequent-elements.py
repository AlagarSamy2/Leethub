class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        print(d)
        d={k:v for k,v in sorted(d.items(),key= lambda x:x[1],reverse=True)}
        list1,i=[],0
        for key,val in d.items():
            list1.append(key)
            if i==k-1:
                break
            
            i+=1
        return list1