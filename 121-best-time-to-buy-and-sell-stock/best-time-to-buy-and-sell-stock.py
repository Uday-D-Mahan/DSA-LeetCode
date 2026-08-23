class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        profit = 0

        for i in range(len(prices)):
            if prices[i] <= smallest:
                smallest = prices[i]

            if prices[i] - smallest > profit:
                profit = prices[i] - smallest

        return profit
                    

                
            
               