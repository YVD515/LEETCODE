class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        digits = []
        nums1 = num
        while nums1 > 0:
            nums1, digit = divmod(nums1, 10)
            digits.append(digit)
        for i in digits:
            if num%i== 0:
                count += 1
        return count
