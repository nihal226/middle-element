class solution:

    def merge(self, arr1, m, arr2, n):

        if m == 0:
            for i in range(n):
                arr1[i]=arr2[i]
            return arr1
                

        if n == 0:
            arr1.sort()
            return arr1

        for i in range(n):
            arr1.append(arr2[i])
        j=0
        while j<len(arr1):
            if arr1[j]==0:
                arr1.pop(j)
            else:
                j+=1
            
        arr1.sort()