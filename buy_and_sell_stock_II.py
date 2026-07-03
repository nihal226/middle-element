class solution:
    def maxProfit(self, prices):
        #Write your code here...
        profit=0
        for i in range (1,len(prices)):
            if prices[i]>prices[i-1]:
                profit=profit+(prices[i]-prices[i-1])
        return profit
            