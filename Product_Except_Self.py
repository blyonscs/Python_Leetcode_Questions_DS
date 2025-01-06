# Leetcode 238, Product of array except self
# Must return product without self for every num in the array
# Must be O(n) time and cannot use division
nums = [1, 2, 3, 4]
# Solution [24, 12, 8, 6]
print(nums)
# O(1) memory if prefix and postfix arrays are not added and the calculation is done in the putput array
class Solution:
    def  productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):  # Getting prefix 
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): # Getting postfix and multipling them
            res[i] *= postfix
            postfix *= nums[i]
        return res
