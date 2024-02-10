class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        count = 0
        num = [x for x in range(1,n+1)]
        num1 = [x for x in num if x%m != 0]
        num2 = [x for x in num if x%m == 0]
        count += sum(num1)
        count -= sum(num2)
        return count
