class solution:
    def canCompleteCircuit(self, charge, energy):
        #Write your code here...
        if sum(charge)<sum(energy):
            return -1
        tank=0
        start=0
        for i in range(len(charge)):
            tank+=charge[i]-energy[i]
            if tank<0:
                start=i+1
                tank=0
        return start
                
     
            