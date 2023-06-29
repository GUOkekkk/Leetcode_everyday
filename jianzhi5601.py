from typing import List


# but how to achieve O(1) space complexity and O(n) time complexity
# we can not use the hash table and BF method
# the time complexity is O(3n)
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        # 1. get the xor of all numbers
        # if only has one number, then the xor is the number
        xor = 0
        for num in nums:
            xor ^= num
        # 2. find the rightmost 1
        mask = 1
        while xor & mask == 0:
            mask <<= 1
        # on this rightmost 1 position, a and b is different
        # 3. divide the numbers into two groups
        a = b = 0
        for num in nums:
            if num & mask == 0:
                a ^= num
            else:
                b ^= num
        return [a, b]
