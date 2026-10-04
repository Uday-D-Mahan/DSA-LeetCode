class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        Vowels = "aeiou"
        window_size = s[:k]
        total = sum(1 for ch in window_size if ch in Vowels)
        maximum = total

        for i in range (k , len(s)):
            
            if s[i-k] in Vowels:
                total -= 1

            if s[i] in Vowels:
                total += 1

            if total > maximum:
                maximum = total

        return maximum
               