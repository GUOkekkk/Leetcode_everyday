# It is a DP problem.
# dp[i] = dp[i-1] + dp[i-2] if 10 <= s[i-2:i] <= 25 else dp[i-1]
# by using the % and // to get the last digit and the rest digits to save the space.
class Solution:
    def translateNum(self, num: int) -> int:
        a = b = 1
        y = num % 10
        while num != 0:
            num //= 10
            x = num % 10
            # temp is the last two digits
            tmp = 10 * x + y
            c = a + b if 10 <= tmp <= 25 else a
            # cause it is invrese order, so we need to change the value of a and b
            a, b = c, a
            y = x
        return a


if __name__ == "__main__":
    num = 12258
    s = Solution()
    print(s.translateNum(num))
