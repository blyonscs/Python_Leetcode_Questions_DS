#Leetcode 167 Two sum II, Given an array sorted in ascending order find the two numbers that add up to the target
numbers = [2, 3, 4, 5, 9, 11, 15] # indices 3 and 4 is the solution, starts at one for this problem
target = 9
print(numbers)

class Solution:
    def  twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1  # left pointer starts at the beggining, right pointer startes at the end

        while l < r:  # if the nuber is bigger than the target, move the right pointer left, if it is smaller do the reverse
            curSum = numbers[l] + numbers[r] # Current sum of the two pointers

            if curSum > target:  # if sum is greater than target move the right pointer the lower the sum
                r -= 1
            elif curSum < target: # if sum is smaller than target move the left pointer the increase the sum
                l += 1
            else:
                return [l + 1, r + 1]  # current sum is equal to the target, add one to each indices to adhere to the question
        return[]
    # linear time solution O(n)