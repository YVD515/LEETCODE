class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n %2 == 0:
            return n
        else:
            return int(n*2)
