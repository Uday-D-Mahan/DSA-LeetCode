class Solution:
    def kthCharacter(self, k: int) -> str:

        def solve(k):
            if k == 1:
                return 0

            half = 1

            while half * 2 < k:
                half *= 2

            return solve(k - half) + 1

        shift = solve(k)

        return chr(ord('a') + shift)