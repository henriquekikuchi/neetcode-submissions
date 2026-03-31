class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        select a single day to buy
        select a different day to sell it in the FUTURE
        return the MAXIUM PROFIT
        i can choose not make any transaction then profit would be 0
        """

        totalDays = len(prices)
        betterProfit = 0
        idxMinPrice, idxPossibleSellDay = 0, 1

        while idxPossibleSellDay < totalDays:
            profit = prices[idxPossibleSellDay] - prices[idxMinPrice]
            
            if profit < 0:
                idxMinPrice = idxPossibleSellDay
                idxPossibleSellDay += 1
            else:
                betterProfit = max(profit, betterProfit)
                idxPossibleSellDay += 1

        return betterProfit
