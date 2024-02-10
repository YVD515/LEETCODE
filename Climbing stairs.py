class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        x1 = 0 
        x2 = 1
        
        last_sum = 1
        for i in range(0, n):
            sum = x1 + x2
            x1 = x2
            x2 = sum
        return sum

        #fibonacci
