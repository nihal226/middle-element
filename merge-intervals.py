class solution:
    def mergeOverlappingIntervals(self, nums):
        #Write your code here...
        nums.sort()
        merged=[]
        for num in nums:
            if not merged:
                merged.append(num)
            elif num[0]<=merged[-1][1]:
                merged[-1][1]=max(merged[-1][1],num[1])
            else:
                merged.append(num)
        return merged
                