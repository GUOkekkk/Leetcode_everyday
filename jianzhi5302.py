from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # print(f"l: {l}, r: {r}, mid: {mid}")
            # if nums[mid] < (nums[l] + nums[r]) / 2:
            if nums[mid] == mid
                l = mid + 1
            else:
                r = mid - 1
        return l


if __name__ == "__main__":
    s = Solution()
    test = [0, 1, 2, 3, 4, 5, 6, 7, 9]

    print(s.missingNumber(test))
