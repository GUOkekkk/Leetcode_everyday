from typing import List


# there are lots of similar problems, buy and sell the stock to get the max profit
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         cost, profit = float("+inf"), 0
#         for price in prices:
#             cost = min(cost, price)
#             profit = max(profit, price - cost)
#         return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # set the cost to the max value, maintain the profit
        cost, profit = int(1e9), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        # dp[i] = max(dp[i-1], prices[i] - min(prices[:i]))
        # dp[0] = 0
        # use the cost to replace the min(prices[:i]) to save the time
        # use the profit to replace the dp[i-1] to save the space
        return profit
