class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.x = x
        x = str(x)
        revX = x[::-1]
        return x == revX            
x = 121
result = Solution().isPalindrome(x)
if result is not False:
    print(f"Input: x = {x}")
    print(f"Output: true")
    print(f"Explanation: {x} reads as {x} from left to right and from right to left.")
else: 
    print(f"Input: x = {x}")
    print(f"Output: false")
    print(f"Explanation: From left to right, it reads {x}. From right to left, it becomes from left to right and from right to left.")
