class Solution:
    def twoSum(self, nums, target: int):
        self.nums = nums
        self.target = target
        for i in nums:
            for j in range(nums.index(i)+1, len(nums)):
                if nums[j]+i == target:
                    a = [nums.index(i), j]
                    return a
                else:
                    continue
            
nums = [2, 7, 11, 15]
target = 9
result = Solution().twoSum(nums, target)
if result is not None:
    print("Input: nums =", nums, ", target =", target)
    print("Output: ", result)
