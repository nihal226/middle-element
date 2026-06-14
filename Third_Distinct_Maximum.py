class solution:
    def findThirdHighest(self, readings):
        # Write your code here...
        s=set(readings)
        if len(s)<3:
            return max(s)
        
        l=list(s)
        l.sort()
        return l[-3]
        