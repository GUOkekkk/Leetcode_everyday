# can not use for, while, if, else, switch, case, ?:, or other control flow statements
# can not use multiplication or division
class Solution:
    def __init__(self):
        self.res = 0

    def sumNums(self, n: int) -> int:
        # use and to replace if, if n > 1 do the recursion, if n == 1, break the recursion
        n > 1 and self.sumNums(n - 1)
        self.res += n
        # self.res is a global variable, so it can be used in the recursion
        return self.res
