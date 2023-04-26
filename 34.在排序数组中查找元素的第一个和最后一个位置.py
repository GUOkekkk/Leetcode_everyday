#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left_func(nums, target):
            n = len(nums) - 1
            left = 0
            right = n
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        a = left_func(nums, target)  # find the target index
        b = left_func(nums, target + 1)  # find the target + 1 index
        if a == len(nums) or nums[a] != target:
            return [-1, -1]
        else:
            return [a, b - 1]


# @lc code=end
