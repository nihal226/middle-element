class solution:
    def printDoubleCenteredStarTriangle(self, n):
        #Write your code here...
        
        
        for i in range(n):
            print(" "*(n-i-1)+"*"*(2*i+1))
        for i in range(n):
            print(" " * i+"*"*(2*n-2*i-1))
if __name__=="__main__":
    n=int(input())
    sol=solution()
    sol.printDoubleCenteredStarTriangle(n)