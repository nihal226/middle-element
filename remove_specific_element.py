class solution:
    def removeSpecificElement(self, arr, target):
        #Write your code here...
        i=0
        while i<len(arr):
            if arr[i]==target:
                arr.pop(i)
            else:
                i+=1
        return len(arr)
        return arr
            