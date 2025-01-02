# Leetcode 202, determine if the number given is a happy number
# A happy number is a number where if you square both sides and add them, and repeat this process over and over again
# it will eventually end up at one
n = 19
print(n)
 # If a number is visited more than once then it is a loop and not happy
 # T = O(n)
class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True
        return False
    

    def sumOfSquares(self, n:int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2 
            output += digit
            n = n // 10
        return output

# fast amd slow pointer solution
# T = O(logn)  M = O(1)
class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.nextNumber(n)
        fast = self.nextNumber(self.nextNumber(n))
     
        while slow != fast:
            if fast == 1: return True
            slow = self.nextNumber(slow)
            fast = self.nextNumber(self.nextNumber(fast))

    def nextNumber(self, n: int) -> int: # Caluculating the next number with mod and division
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2 
            output += digit
            n = n // 10
        return output