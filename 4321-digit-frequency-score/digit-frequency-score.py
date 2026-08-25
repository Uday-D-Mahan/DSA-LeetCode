class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        count = {}

        while n > 0:
            digit = n % 10

            if digit in count:
                count[digit] += 1

            else:
                count[digit] = 1

            n = n // 10

        ans =0


        for digit in count:
            ans += digit * count[digit]

        return ans


         

       

            
