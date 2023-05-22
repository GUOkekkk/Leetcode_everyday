#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

from typing import List

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols

        while left < right:
            i, j = divmod((left + right) // 2, cols)
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                left = i * cols + j + 1
            else:
                right = i * cols + j
        return False
# @lc code=end

if __name__ == "__main__":
    test = Solution()
    print(test.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
