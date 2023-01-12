from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least_sell = float('inf')
        max_prof = 0
        for i in range(len(prices)):
            if prices[i] < least_sell:
                least_sell = prices[i]
            
            profit = prices[i] - least_sell

            if profit > max_prof:
                max_prof = profit

        return max_prof
            

s = Solution()
prices = [2,1,4]
print(s.maxProfit(prices))