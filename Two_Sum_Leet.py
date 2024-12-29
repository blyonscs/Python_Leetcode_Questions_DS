# Leetcode 1 Two sum, find the two sums that add up to the target, assume you hav only one solution and return the indexes
nums = [2, 7, 11, 15]
target = 9
print(nums)

class Solution:
    def  twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val:index

        for i, n in enumerate(nums):  # looking for the diffrence between the n and the target and seeing if it is in the hashmap
            diff  = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return  