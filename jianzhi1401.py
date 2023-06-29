import math


# use the math pow function is faster than *
# 3 is the best number to cut, more close to e, 1-lnx
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return int(math.pow(3, a))
        if b == 1:
            # we change one 3 to 2*2
            return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)
