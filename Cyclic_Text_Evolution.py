class solution:
    def findKthCharacter(self, k):
        # Write your code here...
        shift = bin(k-1).count("1")%26
        return chr(ord("a")+shift)