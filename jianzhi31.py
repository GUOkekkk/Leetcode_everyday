from typing import List


# the key of this question is to find the regularity of the stack
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # use a stack to simulate the process
        stack = []
        i = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack
