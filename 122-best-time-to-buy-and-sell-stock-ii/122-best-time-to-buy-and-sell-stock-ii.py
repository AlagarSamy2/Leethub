class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        val=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                val=val+prices[i]-prices[i-1]
        return val