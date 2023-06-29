# how to deal with the negative number
# but the number is in two's complement
# so we could deal with it as a unsigned number


class Solution:
    def add(self, a: int, b: int) -> int:
        # 0xFFFFFFFF is the maximum number of 32-bit integer
        # cause in python, the integer is not limited by the 32-bit; so we use this to limit the number
        x = 0xFFFFFFFF
        # remove all the over 32-bit number
        a, b = a & x, b & x
        while b != 0:
            # we use the (a ^ b) to get the sum of a and b and use (a & b) << 1 to get the carry
            # it is better to give a list to check the process
            # for the sum, it is like the xor operation
            # for the carry, it is like the and operation and then move the carry to the left
            # until the carry is 0
            # cause we cant not use the + operation, so we use the while loop until the carry is 0
            # it is like every time we give some part of the carry to the sum; the no carry part
            a, b = (a ^ b), (a & b) << 1 & x
        # and if a is negative, it will be considered as over 32-bit number, we need to change it to the 32-bit number
        # so we use ~(a ^ x) to make the number over 32-bit to be 0 and the number less than 32-bit to keep the same
        return a if a <= 0x7FFFFFFF else ~(a ^ x)


if __name__ == "__main__":
    a = -1
    b = 2
    s = Solution()
    print(s.add(a, b))
