class solution:
    def manipulateArray(self, arr, n, k):
        #Write your code here...
        if n%2==0:
            middle=(n//2)-1
            
        
        else:
            middle=n//2
        arr[middle]*=k
        
if __name__=="__main__":
    n, k=map(int,input().split())
    arr=list(map(int,input().split()))
    sol=solution()
    sol.manipulateArray(arr,n,k)
    
    for num in arr:
        print(num, end=" ")