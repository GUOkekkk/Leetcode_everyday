class Solution:
    def numWays(self, n: int) -> int:
        # the satate transfer equation is f(n) = f(n-1) + f(n-2), but this part is a bit wrong, cause we think the start
        # is from 1, but the question is from 0, so we need to change the start point
        a1, a2 = 1, 2
        # this one is the special case
        if n == 0:
            return 1
        for _ in range(1, n):
            a1, a2 = a2, a1 + a2
        return a1 % 1000000007


class Solution:
    def numWays(self, n: int) -> int:
        # the satate transfer equation is f(n) = f(n-1) + f(n-2), but this part is a bit wrong, cause we think the start
        # is from 1, but the question is from 0, so we need to change the start point
        a0, a1 = 1, 1
        for _ in range(n):
            a0, a1 = a1, a0 + a1
        return a0 % 1000000007


if __name__ == "__main__":
    test = Solution()
    print(test.numWays(7))
