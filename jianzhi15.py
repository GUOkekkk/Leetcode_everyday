# use the & and >>
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1  # check if the last bit is 1
            n >>= 1  # move the last bit to the right
        return res


# function
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")


# Brian Kernighan's Algorithm
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            # n-1 will flip the rightmost 1 to 0 and flip all the 0 after the rightmost 1 to 1
            # n & (n-1) will remove the rightmost 1
            # after all the 1 are removed, n will be 0
            n &= n - 1
        return res


if __name__ == "__main__":
    s = Solution()
    s.hammingWeight(11)
