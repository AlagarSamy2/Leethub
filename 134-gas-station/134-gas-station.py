class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        dif=[]
        for i in range(0,len(cost)):
            dif.append(gas[i]-cost[i])
        cur_sum=0
        idx=0
        for i in range(0,len(dif)):
            cur_sum+=dif[i]
            if cur_sum<0:
                cur_sum=0
                idx=i+1
        return idx