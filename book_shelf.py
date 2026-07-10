class solution:

    def placeBooks(self, numBooks, shelfSize):
        # Write your code here...
        
        ans=[]
        def backtrack(start,path):
            if len(path)==shelfSize:
                ans.append(path[:])
                return
            for book in range(start,numBooks+1):
                path.append(book)
                backtrack(book+1,path)
                path.pop()
        backtrack(1,[])
        return ans