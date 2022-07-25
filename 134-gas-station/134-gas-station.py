class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        diff=[]
        for i in range(0,len(gas)):
            diff.append(gas[i]-cost[i])
        total,count=0,0
        for i in range(len(diff)):
            total+=diff[i]
            if total<0:
                total=0
                count=i+1
            # print(total,count)
        return count