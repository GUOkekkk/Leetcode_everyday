#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

from typing import List
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p0, p2 = 0, n - 1
        i = 0
        while i <= p2:
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            i += 1
# @lc code=end

if __name__ == "__main__":
    test = Solution()
    print(test.sortColors([2,0,2,1,1,0]))
