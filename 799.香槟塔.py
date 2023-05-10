#
# @lc app=leetcode.cn id=799 lang=python3
#
# [799] 香槟塔
#

# @lc code=start
class Solution:
    def champagneTower(self, k: int, n: int, m: int) -> float:
        if k == 0:
            return 0
        # can't use this condition, cause the speed is different
        # if k < reduce(lambda x, y: x+y, list(range(1, n+2))) - n:
        #     return 0
        # more space to store info
        f = [[0] * (n + 10) for _ in range(n + 10)]

        f[0][0] = k
        for i in range(n + 1):
            for j in range(i + 1):
                if f[i][j] <= 1:
                    continue
                f[i + 1][j] += (f[i][j] - 1) / 2
                f[i + 1][j + 1] += (f[i][j] - 1) / 2
        return min(f[n][m], 1)
    # @lc code=end
