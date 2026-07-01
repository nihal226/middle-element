class solution:
    def removeDuplicates(self,arr,n):
        #Write your code here...
        i=0
        while i<len(arr)-1:
            if arr[i+1]==arr[i]:
                arr.pop(i)
            else:
                i+=1
        return len(arr)
        return arr
        
  
            
       
        