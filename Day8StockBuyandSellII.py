class Solution:
    def maximumProfit(self, prices):
        # code here
        minprice = prices[0]
        res =0
        for i in range(1,len(prices)):
            minprice = min(minprice, prices[i])
            
            res = max(res,prices[i]-minprice)
        return res