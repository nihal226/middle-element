class solution:
    def countCandyGroups(self, maximumSweetness, candies):
        #Write Your Code Here...
        if maximumSweetness<=1:
            return 0
        count=0
        left=0
        product=1
        for right in range(len(candies)):
            product*=candies[right]
            while product>=maximumSweetness:
                product//=candies[left]
                left+=1
            count+=(right-left+1)
        return count
        