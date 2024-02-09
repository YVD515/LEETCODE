class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = sum(range(0, len(nums)+1))
        _ = 0
        for j in nums:
            _ += j
        return l-_
