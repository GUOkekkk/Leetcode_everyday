from typing import List


# solve use the two pointer
# more space
# class Solution:
#     def exchange(self, nums: List[int]) -> List[int]:
#         odd, even = 0, len(nums) - 1
#         res = [0] * len(nums)
#         for i in range(len(nums)):
#             if nums[i] % 2 == 0:
#                 res[even] = nums[i]
#                 even -= 1
#             else:
#                 res[odd] = nums[i]
#                 odd += 1
#         return res


# use the & operator to replace the % operator could speed up the program
# & 1 == % 2
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        even, odd = 0, len(nums) - 1
        while even < odd:
            if (nums[even] & 1 == 0) and (nums[odd] & 1 == 1):
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 1
                odd -= 1
            if nums[even] & 1 == 1:
                even += 1
            if nums[odd] & 1 == 0:
                odd -= 1
        return nums


if __name__ == "__main__":
    test = Solution()
    nums = [1, 2, 3, 4]
    print(test.exchange(nums))
