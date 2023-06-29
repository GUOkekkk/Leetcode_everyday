from typing import List


# 1. sort and return the middle one -> time: O(nlogn) space: O(1)
# 2. hash table -> time: O(n) space: O(n)
# 3. Boyer-Moore Voting Algorithm -> time: O(n) space: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0:
                x = num
            votes += 1 if num == x else -1
        return x
