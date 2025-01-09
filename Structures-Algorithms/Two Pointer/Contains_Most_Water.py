# Leetcode 11 Container with most water, given non-negitive integers
# Find two lines that together with the x-axis would contain the most water
height = [1,8,6,2,5,4,8,3,7]
# output = 49
print(height)

class Solution:
    def  maxArea(self, height: List[int]) -> int:
        res = 0  # initializing result variable
        l, r = 0, len(height) - 1  # putting two pointers on both sides of the array

        while l < r:
            area = (r - l) * min(height[l], height[r]) # finding area
            res = max(res, area) # updates res if needed

            if height[l] < height[r]:  # moves the pointer with the smallest height
                l += 1
            else:
                r -= 1

        return res