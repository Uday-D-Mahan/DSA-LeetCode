class Solution:
    def maxFreqSum(self, s: str) -> int:
        count = {}
        vowels = ("a","e","i","o","u")
        
        for char in s:
            if char in count:
                count[char] += 1

            else:
                count[char] = 1

        high1 = 0
        high2 = 0

        for char in count:
            if char in vowels:
                high1 = max(high1, count[char])

            else:
                high2 = max(high2, count[char])

        return high1 + high2

        
