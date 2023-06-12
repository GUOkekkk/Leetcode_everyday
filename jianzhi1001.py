# when it is a dp problem, we need to find the state transfer equation
class Solution:
    def fib(self, n: int) -> int:
        a0, a1 = 0, 1
        # range(0, n) is [0, n-1]
        # the for loop will run n times, is one-step faster than f(n), the a1 is f(n+1)
        for _ in range(0, n):
            a0, a1 = a1, a0 + a1
        # to limit the result
        return a0 % 1000000007


if __name__ == "__main__":
    test = Solution()
    print(test.fib(5))
