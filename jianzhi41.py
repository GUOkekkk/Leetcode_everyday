class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        n = len(self.arr)
        if n % 2 == 0:
            return (self.arr[n // 2 - 1] + self.arr[n // 2]) / 2
        else:
            return self.arr[n // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# use the heap to store the half of the array
from heapq import *


class MedianFinder:
    def __init__(self):
        self.A = []  # small heap, save the bigger half
        self.B = []  # big heap, save the smaller half

    # the heap is supposed to be the small heap, so we need to reverse the sign of the elements in the big heap
    def addNum(self, num: int) -> None:
        # we always keep the length of the small heap is equal to or one more than the big heap
        # so if the lenA == lenB, we should insert the num into the small heap
        # but if we insert it directly, it will break the property of the heap
        # so we insert it to the big heap first, then pop the biggest element in the big heap and insert it to the small heap
        # when the lenA != lenB, we should insert the num into the big heap and do the similar steps
        if len(self.A) != len(self.B):
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))
        else:
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))

    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0
