class solution:
    def printDescendingLetterTriangle(self, n):
        #Write your code here...
        
        
        for i in range(n):
            for j in range(n-i):
                print(chr(65+j),end=" ")
            print()
if __name__=="__main__":
    n=int(input())
    sol=solution()
    sol.printDescendingLetterTriangle(n)