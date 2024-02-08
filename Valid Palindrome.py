class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        s = [x for x in s if x.isalnum()==True]
        if s == s[::-1]:
            return True
        return False
