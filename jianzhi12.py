# it is a martix search problem, and typically we can use dfs to solve it or BFS
# DFS could solve this problem but it is a bit time consuming we could use the cutting branch method
# if out of matrix -> cut, if it is not the in the str -> cut, if visited -> cut(how to mark visited? -> change to ' ', cause we do not need keep the mateix)
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            # reach the end of the word
            if k == len(word) - 1:
                return True
            # mark the visited
            board[i][j] = " "
            # search the next word, search four directions but actually we only need to search three directions, one is visited
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            # recover the visited, this part is very important for the backtracking problem
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
