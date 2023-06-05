class MinStack:
    def __init__(self):
        # use B to keep the min is O(1)
        self.A, self.B = [], []

    def push(self, x: int) -> None:
        self.A.append(x)
        # the key part is here
        # if the B is empty or the new element is smaller than the last element of B
        if not self.B or self.B[-1] >= x:
            self.B.append(x)

    def pop(self) -> None:
        # A and B pop the minimum element at the same time
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]
