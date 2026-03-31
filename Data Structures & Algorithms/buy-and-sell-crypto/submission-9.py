class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        select a single day to buy
        select a different day to sell it in the FUTURE
        return the MAXIUM PROFIT
        i can choose not make any transaction then profit would be 0
        """

        n = len(prices)

        maximum_profit = -sys.maxsize

        for i in range(n):
            profit = 0
            for j in range(i+1, n):
                profit = prices[j] - prices[i]
                maximum_profit = max(profit, maximum_profit)

        return maximum_profit if maximum_profit > 0 else 0
