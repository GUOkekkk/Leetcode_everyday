#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            profit += max(0, tmp)
        return profit


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.maxProfit([7, 1, 5, 3, 6, 4]))
