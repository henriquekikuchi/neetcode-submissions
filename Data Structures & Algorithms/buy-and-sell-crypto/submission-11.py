class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        select a single day to buy
        select a different day to sell it in the FUTURE
        return the MAXIUM PROFIT
        i can choose not make any transaction then profit would be 0
        """

        n = len(prices)
        maximum_profit = 0
        left, right = 0, 1

        while right < n:
            profit = prices[right] - prices[left]
            
            if profit < 0:
                left = right
                right += 1
            else:
                maximum_profit = max(profit, maximum_profit)
                right += 1

        return maximum_profit
