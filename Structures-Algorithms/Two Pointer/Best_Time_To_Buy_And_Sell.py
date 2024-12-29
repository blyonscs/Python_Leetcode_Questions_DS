# Leetcode 121 Best time to buy and sell a stock, pick the best time in an array to but and stock and sell it for maximum profit
# Two Pointer solution, best diffrence from left to right, mem : 0  time: O(n)
prices = [7, 1, 5, 3, 6, 4, 1]
print(prices)

class Solution:
    def  twoSum(self, prices: List[int]) -> int:
       l, r = 0, 1 #l = buying, r = selling
       MaxP = 0

       while r < len (prices):
           if prices[l] < prices [r]:
               profit = prices[r] = prices[l]
               MaxP = max(MaxP, profit) # checking if the profit is bigger then the current max
           else:   # no profit, is a loss
               l = r  
       r += 1
       
       return MaxP
       

       
