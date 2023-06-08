class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = 0
        for i in nums:
            if i == target:
                ans += 1
        return ans

    # nums.count(target)


# it is a ordered list so could use the binary search
class Solution:
    def search(self, nums: [int], target: int) -> int:
        def helper(tar):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if nums[m] <= tar:
                    i = m + 1
                else:
                    j = m - 1
            return i

        return helper(target) - helper(target - 1)
