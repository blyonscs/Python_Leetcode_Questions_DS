#Leetcode 242 Valid Anagram, Given two strings s and t, return true if t is an anagram of s, and false otherwise
s = "anagram", t = "nagaram" # output = true
# most efficient solution
class Solution:
    def  isAnagram(self, s: str, t : str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
    # Speed O(N)/O(s+t) memory is the same

# One line solution in python
# Counter(s) == Counter(t)


# Solution in memory O(1)
class Solution:
    def  isAnagram(self, s: str, t : str) -> bool:
       return sorted(s) == sorted(t)