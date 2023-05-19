#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

from typing import List

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0] * (1 << n) # move to n bits
        print(1 << n)
        for i in range(1 << n):
            # i >> 1: move to right 1 bit, remove the last bit
            print(i, i >> 1, i ^ (i >> 1))
            ans[i] = (i >> 1) ^ i
        return ans
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.grayCode(3))
