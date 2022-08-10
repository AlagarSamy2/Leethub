class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        def dfs(i,canbuy):
            if i>=len(prices):
                return 0
            if (i,canbuy) in dp: # This one is used for selling
                return dp[(i,canbuy)]
            if canbuy is True:#we can buy
                buy=dfs(i+1,not canbuy)-prices[i]#we bought
                cooldown=dfs(i+1,canbuy)
                dp[(i,canbuy)]=max(buy,cooldown)
            else:
                sell=dfs(i+2,not canbuy)+prices[i]
                cooldown=dfs(i+1,canbuy)
                dp[(i,canbuy)]=max(sell,cooldown)
            return dp[(i,canbuy)]
        return (dfs(0,True))#We can buy first stock
        
                
        