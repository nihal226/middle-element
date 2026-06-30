class solution:
    def leftRotate(self, arr, n, k):
        #Write your code here...
        k=k%n
        temp=arr[:k]
        arr[:n-k]=arr[k:]
        arr[n-k:]=temp
    