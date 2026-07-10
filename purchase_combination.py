class solution:
    def purchaseCombinations(self, prices, budget):
        #Write Your Code Here...
        
        
        ans=[]
        def backtrack(start,path,total):
            if total==budget:
                ans.append(path[:])
                return
            if total>budget:
                return
            for i in range(start,len(prices)):
                path.append(prices[i])
                backtrack(i,path,total+prices[i])
                path.pop()
        backtrack(0,[],0)
        return ans