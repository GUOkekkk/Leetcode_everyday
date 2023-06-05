class CQueue:
    def __init__(self):
        # two stacks to simulate the queue
        # use A to store the elements but use the B to pop the elements as a queue
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        # for the stack and the queue, the append is the same
        # in python the append and pop is like a stack
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B:
            return self.B.pop()
        if not self.A:
            return -1

        # initialize the stack B
        while self.A:
            # inverse the order of the stack
            self.B.append(self.A.pop())
        return self.B.pop()
