class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        nums = [x for x in range(1, n+1)]
        num1 = [x for x in nums if x%3 == 0 or x%5 ==0 or x%7 == 0]
        count += sum(num1)
        return count
