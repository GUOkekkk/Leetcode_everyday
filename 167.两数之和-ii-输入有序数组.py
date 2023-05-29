#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

from typing import List


# @lc code=start
# This method is stupied slow and space consuming
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         n = len(numbers)
#         for i in range(n):
#             if target - numbers[i] in numbers[i + 1 :]:
#                 return [i + 1, numbers[i + 1 :].index(target - numbers[i]) + i + 2]


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1


# @lc code=end

if __name__ == "__main__":
    test = Solution()
    print(test.twoSum([2, 7, 11, 15], 9))
