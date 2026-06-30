class solution:
    def moveZerosToEnd(self, arr, n):
        #Write your code here...
       
        v=[]
        for i in range(n):
            if arr[i]!=0:
                v.append(arr[i])
        v.sort()
        diff=n-len(v)
        
        v.extend([0]*diff)
        

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    sol = solution()
    sol.moveZerosToEnd(arr, n)
    for i in range(n):
        print(arr[i], end=" ")
