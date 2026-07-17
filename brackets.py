class solution:

    def generateBrackets(self, m):
        # Write your code here...
        ans=[]
        def backtrack(curr,open_used,close_used):
            if len(curr)==2*m:
                ans.append(curr)
                return
            if open_used<m:
                backtrack(curr+"[",open_used+1,close_used)
            if close_used<open_used:
                backtrack(curr+"]",open_used,close_used+1)
        backtrack("",0,0)
        return ans