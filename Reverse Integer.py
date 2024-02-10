class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = []
        ret = 0
        if x > 0:
            while x > 0:
                x, digit = divmod(x, 10)
                num.append(digit)
            for i in range(0, len(num)):
                ret += num[i]*10**(len(num)-1-i)
            if ret <= 2**31-1:
                return ret
            else:
                return 0
        else:
            x = -x
            while x > 0:
                x, digit = divmod(x, 10)
                num.append(digit)
            for i in range(0, len(num)):
                ret += num[i]*10**(len(num)-1-i)
            ret = -ret
            if ret >= -2**31:
                return ret
            else:
                return 0

