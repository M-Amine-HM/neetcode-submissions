class Solution(object):
    def maxProfit(self, prices):
        maxProfit=0
        profit=0
        b=0
        s=0
        for i in range(len(prices)) :
            for j in range(i+1,len(prices)) :
                profit=prices[i]-prices[j]
                if maxProfit>profit : 
                    maxProfit=profit
                    b=i
                    s=j
        return abs(maxProfit)