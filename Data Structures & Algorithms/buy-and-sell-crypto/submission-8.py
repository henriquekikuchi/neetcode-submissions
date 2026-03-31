class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2: return 0
        
        i, j = 0, 1
        maxProfit = 0

        while i < len(prices) and j < len(prices):
            if prices[j] < prices[i]:
                i = j
                j = i + 1
            elif prices[i] == prices [j]:
                j += 1
            else:
                maxProfit = max(maxProfit, prices[j] - prices [i])
                j += 1
        return maxProfit
