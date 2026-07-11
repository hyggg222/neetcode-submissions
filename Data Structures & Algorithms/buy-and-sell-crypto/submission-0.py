class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Min = prices[0]
        Profit = 0
        for i in range(1, len(prices)):
            if prices[i] > Min:
                Profit = max(Profit, prices[i] - Min)
            Min = min(Min, prices[i])
        return Profit