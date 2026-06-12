class solution:
    def printAlternatingBinaryTriangle(self, n):
        #Write your code here...
        
        
        for i in range(n):
            k=1 if i%2==0 else 0
            for j in range(i+1):
                print(k,end=" ")
                k=1-k
            print()
if __name__ == "__main__":
    n = int(input())
    sol = solution()
    sol.printAlternatingBinaryTriangle(n)