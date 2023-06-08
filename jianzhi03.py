from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dum = []
        for i in nums:
            if i not in dum:
                dum.append(i)
            else:
                return i
        return -1


# class Solution:
#     def findRepeatNumber(self, nums: [int]) -> int:
#         i = 0
#         while i < len(nums):
#             if nums[i] == i:
#                 i += 1
#                 continue
#             if nums[nums[i]] == nums[i]: return nums[i]
#             nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
#         return -1
