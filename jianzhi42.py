from typing import List


# it is a DP problem
# dp[i] stores the max sum of the subarray ending with nums[i]
# if the dp[i-1] is negative, then we should not use it, the nums[i] is enough
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            # if the previous sum is negative, then we should not use it
            # so we just use the current value
            nums[i] += max(nums[i - 1], 0)
        return max(nums)
