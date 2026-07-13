class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP=0
        maxP=0
        profit=0
        for i in range(1,len(prices)) :
            if prices[maxP]<prices[i] and maxP>=minP :
                maxP=i
            if prices[minP]>prices[i] and maxP>=minP:
                minP=i
            profit=prices[maxP]-prices[minP]
        return profit
                
