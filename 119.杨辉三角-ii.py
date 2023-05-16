#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        list = [1] * (rowIndex + 1)
        for i in range(1, rowIndex + 1):
            list[i] = list[i - 1] * (rowIndex - i + 1) // i
        return list
# @lc code=end
