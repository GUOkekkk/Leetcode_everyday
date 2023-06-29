from typing import List


# #  A easy way, just record the number of 1 in each bit, and then mod 3, the result is the bit of the single number.
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         counts = [0] * 32
#         for num in nums:
#             for j in range(32):
#                 # when we say the bit of the number, we start from the right
#                 # check the jth bit of num
#                 counts[j] += num & 1
#                 # right shift num
#                 num >>= 1
#         res, m = 0, 3
#         for i in range(32):
#             # left shift res
#             res <<= 1
#             # add the bit of the single number
#             # cause we have to preocess the bit number, so we need use the or operation to keep the 1
#             res |= counts[31 - i] % m  # 0 or 1 cause the number only could be 0, 1, 3, 4
#         # special case for the negative number, if the first one is not 0, means it is a negative number
#         # if counts[31] % m == 0 means the first bit is 0, so we just return res
#         return res if counts[31] % m == 0 else ~(res ^ 0xFFFFFFFF)


# the Finite State Machine
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        # we use the two one to store the state of each bit
        # get a list to know how the state transfer
        # 00 -> 01 -> 10 -> 00
        # if two == 0:
        #     if n == 0:
        #         one = one
        #     if n == 1:
        #         one = ~one
        # if two == 1:
        #     if n == 0:
        #         one = 0
        #     if n == 1:
        #         one = 0
        # then simplify the state transfer
        # one = one ^ n & ~two # hard to think
        # for two it is based on the new one and list it out and simplify it
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones


if __name__ == "__main__":
    test = Solution()
    print(test.singleNumber([3, -4, 3, 3]))
