from typing import List


# the problem is that we cannot use division
# if we could use the division, we can just calculate the product of all elements and divide it by the current element
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        # initialize the list
        b, tmp = [1] * len(a), 1
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1]  # calculate the below triangle
        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1]  # calculate the above triangle
            b[i] *= tmp  # multiply the above and below triangle
        return b
