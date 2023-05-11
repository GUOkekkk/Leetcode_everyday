#
# @lc app=leetcode.cn id=313 lang=python3
#
# [313] 超级丑数
#

# @lc code=start
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        m = len(primes)
        # dp[i] 代表第i+1个丑数
        dp = [1] * n
        # 丑数, 刚刚乘过的丑数的坐标, 质因数
        pq = [(p, 0, i) for i,p in enumerate(primes)]

        for i in range(1, n):
            # 目前最新的最小的丑数
            dp[i] = pq[0][0]
            # 所有等于这个值的要全部出队列，并根据该乘的丑数重新加入队列
            while pq and pq[0][0] == dp[i]:
                _, idx, p = heapq.heappop(pq)
                heapq.heappush(pq, (dp[idx+1] * primes[p], idx + 1, p))
        return dp[-1]
# @lc code=end
