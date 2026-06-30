class solution:
    def maxAmount(self, n, arr):
        #Write your code here...
        case1=self.solve(arr[:-1])
        case2=self.solve(arr[1:])
        return max(case1,case2)
        
        
    def solve(self,arr): 
        p2=arr[0]
        n=len(arr)
        if n==1:
            return p2
        p1=max(arr[0],arr[1])
        for i in range(2,n):
            pick=arr[i]+p2
            not_pick=p1
            cur=max(pick,not_pick)
            
            p2=p1
            p1=cur
        return cur