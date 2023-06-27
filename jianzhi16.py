# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         # special case(important for this problem)
#         def helper(x, n):
#             if n == 1:
#                 return x
#             if n == 0:
#                 return 1
#             if n < 0:
#                 return 1 / helper(x, -n)
#             # speed up
#             # when the n is the even number
#             if n % 2 == 0:
#                 return helper(x * x, n // 2)
#             # when the n is the odd number
#             else:
#                 return x * helper(x, n - 1)

#         return helper(x, n)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # special case(important for this problem)
        if x == 0:
            return 0

        res = 1

        # deal with the negative number
        if n < 0:
            x, n = 1 / x, -n

        # use the bit operation to speed up
        # n&1 -> n%2
        # until n == 0 break the loop
        while n:
            if n & 1:
                res *= x
            # the return is the res, should be clear about the process
            x *= x
            # n = n // 2
            n >>= 1
        return res


# the time complexity is O(n) we need to decrease the time complexity to O(logn)
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         # special case(important for this problem)
#         # we can not use the ** operator
#         # the hard part is the negative number
#         if n == 0:
#             return 1
#         ans = x
#         for i in range(1, abs(n)):
#             ans *= x
#         if n < 0:
#             return 1 / ans
#         else:
#             return ans


if __name__ == "__main__":
    test = Solution()
    print(test.myPow(2.00000, 10))
