class solution:
    def printSquarePattern(self, n):
        #Write your code here...
        for i in range(n):
            for j in range(n):
                print("*",end="")
            print()
n=int(input())
sol=solution()
sol.printSquarePattern(n)