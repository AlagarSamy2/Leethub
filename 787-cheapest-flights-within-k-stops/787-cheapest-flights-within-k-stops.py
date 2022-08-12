class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices=[float('inf')]*n
        prices[src]=0
        
        for i in range(k+1):
            temp=prices.copy()
            for source,dest,price in flights:
                if prices[source]+price <temp[dest]:
                    temp[dest]=prices[source]+price  
            prices=temp
        if prices[dst] == float('inf'):
            return -1
        return prices[dst] 
        