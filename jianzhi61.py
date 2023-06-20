from typing import List


# Rules:
# 1. besides 0, there should be no duplicates
# 2. max - min < 5
# 3. Actually this is not like a real poker game, more like finding a straight line in a list from 0 to 13 and 0 could replace any number


# class Solution:
#     def isStraight(self, nums: List[int]) -> bool:
#         # besides 0, there should be no duplicates
#         # max - min < 5
#         joker_num = 0
#         nums.sort()
#         for i in range(len(nums) - 1):
#             if nums[i] == 0:
#                 # check the joker number
#                 joker_num += 1
#             # if there is a duplicate, return False directly
#             elif nums[i] == nums[i + 1]:
#                 return False
#         return nums[-1] - nums[joker_num] < 5


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        ma, mi = 0, 14
        joker_num = 0
        for num in nums:
            if num == 0:
                joker_num += 1
                continue  # skip the joker number
            ma = max(ma, num)  # remember the max number
            mi = min(mi, num)  # remember the min number
            if num in repeat:
                return False  # if there is a duplicate, return False directly
            repeat.add(num)  # add the number into the set
        # more real poker game
        # for the special case, using the simulation is better than finding the regular pattern
        if 1 in repeat:
            nums.remove(1)
        if 13 in repeat:
            nums.remove(13)
        if 12 in repeat:
            nums.remove(12)
        if 11 in repeat:
            nums.remove(11)
        if 10 in repeat:
            nums.remove(10)
        if len(nums) == joker_num:
            return True
        return ma - mi < 5  # max - min < 5


if __name__ == "__main__":
    nums = [0, 10, 1, 13, 12]
    solution = Solution()
    print(solution.isStraight(nums))
