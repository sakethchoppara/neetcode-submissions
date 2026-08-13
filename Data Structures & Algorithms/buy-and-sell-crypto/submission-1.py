class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            sell = prices[i]
            for j in range(len(prices[:i])):
                buy = prices[j]
                temp = sell-buy
                profit = temp if profit < temp else profit
        return profit
