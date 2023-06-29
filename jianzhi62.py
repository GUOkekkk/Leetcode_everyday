# simulates the process of elimination is time consuming
# we use the dp and the math method to solve this problem
# dp: f(n, m) = (f(n - 1, m) + m) % n
# dp[i] = (dp[i - 1] + m) % i
# the start of the next round is t = m % n
# so the x = (x + t) % n
# so if the ans of the n - 1 is x, the ans of the n is (x + t) % n
# f(n, m) = (f(n - 1, m) + t) % n
# f(n, m) = (f(n - 1, m) + m % n) % n
# f(n, m) = (f(n - 1, m) + m) % n
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        x = 0
        for i in range(2, n + 1):
            x = (x + m) % i
        return x
