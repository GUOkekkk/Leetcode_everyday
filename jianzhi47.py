from typing import List


# It is a DP problem, just use the dp[i][j] to represent the max value of the grid[i][j]
# and modify on the original grid directly to save the space
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                # the first row and only could go from the left
                if i == 0:
                    grid[i][j] += grid[i][j - 1]
                # the first column and only could go from the top
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                # the other cases could go from the left or top
                else:
                    grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]
