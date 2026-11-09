class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l_price = prices[0]
        for idx in range(1, len(prices)):
            p = prices[idx]
            profit = max(profit, (p - l_price))
            l_price = min(l_price, p)

            
        

        # profit += (prices[right-1] - prices[left])
        return profit
        