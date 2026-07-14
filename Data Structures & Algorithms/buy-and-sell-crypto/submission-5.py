class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        mi = 0
        ma = 0
        for i in range(1, len(prices)):
            if  prices[i] - prices[mi] > maxProfit:
                ma = i
                maxProfit = prices[ma] - prices[mi]
                print(maxProfit)
            if prices[mi] > prices[i]:
                mi = i
                print(mi)
        return maxProfit
    #return(maxProfit(prices))