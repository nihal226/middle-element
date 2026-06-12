class solution:
    def printAscLetterTriangle(self, n):
        #Write your code here...
        for i in range(n):
            for j in range(i+1):
                print(chr(65+i),end=" ")
            print()
if __name__=="__main__":
    n=int(input())
    sol=solution()
    sol.printAscLetterTriangle(n)