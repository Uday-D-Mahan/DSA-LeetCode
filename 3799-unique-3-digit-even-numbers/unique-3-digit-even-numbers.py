class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = set()

        def solve(num, used):
            if len(num) == 3:
                if num[-1] % 2 == 0:
                    ans.add(tuple(num))
                return

            for i in range(len(digits)):
                if i in used:
                    continue

                if len(num) == 0 and digits[i] == 0:
                    continue

                used.add(i)
                solve(num + [digits[i]], used)
                used.remove(i)

        solve([], set())

        return len(ans)


            
        