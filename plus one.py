class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        self.digits = digits
        j = ""
        for i in digits:
            i = str(i)
            j += i
        j = int(j)
        k = j + 1
        k = str(k).replace('', ' ').split()
        for p in range(len(k)):
            k[p] = int(k[p])
        return k 
        print(k)
digits = [1,2, 3]
result = Solution().plusOne(digits)
