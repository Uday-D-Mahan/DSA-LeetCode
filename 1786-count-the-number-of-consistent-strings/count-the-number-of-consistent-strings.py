class Solution:
    def countConsistentStrings(self, allowed, words):
        freq = {}
        ans = 0

        # Count characters in allowed
        for char in allowed:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        # Check each word
        for word in words:
            good = True

            for char in word:
                if char not in freq:
                    good = False
                    break

            if good:
                ans += 1

        return ans