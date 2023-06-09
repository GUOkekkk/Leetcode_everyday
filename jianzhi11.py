from typing import List


# when it is a ordered list, we can use binary search
# this question is to find the rotation point
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if not numbers:
            return None
        if len(numbers) == 1:
            return numbers[0]

        l, r = 0, len(numbers) - 1
        while l <= r:
            mid = (l + r) // 2
            if numbers[mid] > numbers[r]:
                l = mid + 1
            elif numbers[mid] < numbers[r]:
                r = mid
            else:
                r -= 1
        return numbers[l]


# when use the binary search, draw the graph to find the rule
# class Solution:
#     def minArray(self, numbers: [int]) -> int:
#         i, j = 0, len(numbers) - 1
#         while i < j:
#             m = (i + j) // 2
#             if numbers[m] > numbers[j]: i = m + 1
#             elif numbers[m] < numbers[j]: j = m
#             else: j = j-1
#         return numbers[i]


if __name__ == "__main__":
    test = Solution()
    print(test.minArray([3, 4, 5, 1, 2]))
