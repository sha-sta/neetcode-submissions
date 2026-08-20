class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 0
        high = 1
        profit = 0
        if len(prices) <= 1:
            return 0
        while high < len(prices):
            if prices[low] > prices[high]:
                low = high
                high += 1
            elif prices[high] - prices[low] > profit:
                profit = prices[high] - prices[low]
                high += 1
            else:
                high += 1
        return profit