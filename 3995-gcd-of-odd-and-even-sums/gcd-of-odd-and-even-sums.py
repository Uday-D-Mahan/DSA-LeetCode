
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        num = 0

        odd = 0
        even = 0

        odd_num = 1
        even_num = 2

        for i in range(n):
            odd += odd_num
            even += even_num

            odd_num += 2
            even_num += 2

        for i in range(1, min(odd, even) + 1):
            if odd % i == 0 and even % i == 0:
                num = i

        return num





