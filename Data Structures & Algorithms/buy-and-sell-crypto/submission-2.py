class Solution(object):
    def maxProfit(self, prices):
        buy=prices[0]
        max=0
        for i in range(1,len(prices)):
            if (prices[i]>buy) :
                if (prices[i]-buy>max) :
                    max=prices[i]-buy
            else :
                buy=prices[i]
        return max
