class solution:
    def maximizeShareProfit(self,arr):
        #Write your code here...
        minimum=arr[0]
        maxProfit=0
        for i in range(1,len(arr)):
            profit=arr[i]-minimum
            maxProfit=max(profit,maxProfit)
            minimum=min(minimum,arr[i])
        return maxProfit
       