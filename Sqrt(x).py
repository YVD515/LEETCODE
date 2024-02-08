import math
class Solution(object):
    def mySqrt(self, x):
        self.x = x
        if x >= 0 and x <= 2**31 - 1:
            return int(math.floor(math.sqrt(x)))
        
