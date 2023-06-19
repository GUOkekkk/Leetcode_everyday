from typing import List


# overtime
# take care if it is a ordered list!!!
# it is a ordered list could use two pointer
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            # it might overflow use nums[l] == target - nums[r]
            # (left + right) / 2 可以用left + ((right - left) >> 1)
            if nums[l] + nums[r] == target:
                return [nums[l], nums[r]]
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
        # maybe the res is empty
        return []


# try this example:[14,15,16,22,53,60] 76
if __name__ == "__main__":
    test = Solution()
    print(test.twoSum([14, 15, 16, 22, 53, 60], 76))
    left = 10
    right = 10

    print(left + ((right - left) >> 1))
