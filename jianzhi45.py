from typing import List


# it is just a sort problem, but the sort rule is different, need to define the sort rule
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        # quick sort
        def quick_sort(l, r):
            # break condition, the array is empty or only one element
            if l >= r:
                return

            i, j = l, r
            while i < j:
                # sort rule -> find the element should be in the front of the nums[l]
                while i < j and nums[j] + nums[l] >= nums[l] + nums[j]:
                    j -= 1
                while i < j and nums[i] + nums[l] <= nums[l] + nums[i]:
                    i += 1
                # swap the nums[i] and nums[j], but actually i == j
                nums[i], nums[j] = nums[j], nums[i]
            nums[i], nums[l] = nums[l], nums[i]
            # quick sort the left and right part / partition
            quick_sort(l, i - 1)
            quick_sort(i + 1, r)

        # map the int to str
        nums = list(map(str, nums))
        quick_sort(0, len(nums) - 1)
        return "".join(nums)


# ? Python built-in sort
# class Solution:
#     def minNumber(self, nums: List[int]) -> str:
#         def sort_rule(x, y):
#             a, b = x + y, y + x
#             if a > b: return 1
#             elif a < b: return -1
#             else: return 0

#         strs = [str(num) for num in nums]
#         strs.sort(key = functools.cmp_to_key(sort_rule))
#         return ''.join(strs)


if __name__ == "__main__":
    nums = [3, 30, 34, 5, 9]
    print(Solution().minNumber(nums))
