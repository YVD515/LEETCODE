class Solution(object):
    def addBinary(self, a, b):
        return bin(add(int(a,2),int(b,2)))[2:]
        
