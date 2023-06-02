#
# @lc app=leetcode.cn id=975 lang=python3
#
# [975] 奇偶跳
#
from typing import List

# @lc code=start
class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:

        def get_jump_location(B):
            ans = [-1] * len(A)
            stack = []

            for i in B:
                while stack and i > stack[-1]:
                    # pop the top element from stack, and the stack_pop will jump to i
                    # keep the extremum
                    stack_top = stack.pop()
                    ans[stack_top] = i
                stack.append(i)
            return ans

        N = len(A)

        # sort B based on the value of A[i], ascending order
        B = sorted(range(N), key=lambda i: A[i])

        # for the odd jump, find the next greater element
        odd_next = get_jump_location(B)

        # sort B based on the value of A[i], descending order
        B.sort(key=lambda i: -A[i])

        # for the even jump, find the next smaller element
        even_next = get_jump_location(B)

        # odd[i]/ even[i] 为DP数组，代表从i进行奇数/偶数跳跃时能否到达末尾。
        odd = [False] * N
        even = [False] * N

        # 根据题意，数组末尾默认为好的起始索引
        odd[N - 1] = even[N - 1] = True

        for i in range(N - 2, -1, -1):
            # 注意一定要从数组倒数第二位开始倒着遍历，因为只有数组末尾的初始化状态是正确的，倒着遍历才能正确转移DP状态。
            # odd firt then even
            if odd_next[i] != -1:
                # 先从odd_next拿到下一个能跳到的节点。接下来要进行偶数跳跃了，查询even，看看能不能跳到末尾。
                next_index = odd_next[i]
                odd[i] = even[next_index]
                # print(f"odd is {odd}")
            if even_next[i] != -1:
                next_index = even_next[i]
                even[i] = odd[next_index]
                # print(f"even is {even}")

        return sum(odd)
# @lc code=end

if __name__ == "__main__":
    test = Solution()
    print(test.oddEvenJumps([10,13,12,14,15]))
