# Leetcode 217 Contains Duplicate, return true if a value appears more than once, return false otherwise
nums = [1, 2, 3 ,1]
print(nums)

class Solution:
    def  containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set() # Adding hashset

        for n in nums: # Iterating through nums
            if n in hashset: # Check if number is already in hashset
                return True
            hashset.add(n) # Add number to hashset
        return False
    # This solution is T = O(n) Mem/Space = O(n) because you have to add numbers to the hashset