class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        ans = 0
        num1 = 0
        num2 = 0
        for i in range (1 , n+1):
            if i % m == 0:
                num1 += i 

            else:
                num2 += i

        ans += num2 - num1
        return ans
            
