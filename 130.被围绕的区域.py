#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

from typing import List


# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        rows, cols = len(board), len(board[0])

        def dfs(x, y):
            # only find the "O" on the edge
            if not 0 <= x < rows or not 0 <= y < cols or board[x][y] != "O":
                return

            board[x][y] = "A"
            # search the four directions
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        # search from the edge
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)

        for i in range(cols - 1):
            dfs(0, i)
            dfs(cols - 1, i)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"


"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        n, m = len(board), len(board[0])

        # use the deque to store the "O" on the edge
        que = collections.deque()

        ### ???
        for i in range(n):
            # the first column
            if board[i][0] == "O":
                que.append((i, 0))
                board[i][0] = "A"
            # the last column
            if board[i][m - 1] == "O":
                que.append((i, m - 1))
                board[i][m - 1] = "A"


        for i in range(m - 1):
            # the first row
            if board[0][i] == "O":
                que.append((0, i))
                board[0][i] = "A"
            # the last row
            if board[n - 1][i] == "O":
                que.append((n - 1, i))
                board[n - 1][i] = "A"

        while que:
            x, y = que.popleft()
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= mx < n and 0 <= my < m and board[mx][my] == "O":
                # pop drom the queue and search the four directions, left pop, right append -> BFS
                    que.append((mx, my))
                    board[mx][my] = "A"

        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
"""

# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    test = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]

    solu.solve(test)

    print(test)
