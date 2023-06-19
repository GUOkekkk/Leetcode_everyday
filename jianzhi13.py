# DFS
# class Solution:
#     def movingCount(self, m: int, n: int, k: int) -> int:
#         def dfs(i, j, si, sj):
#             if i >= m or j >= n or k < si + sj or (i, j) in visited:
#                 return 0
#             visited.add((i, j))
#             # use a trick to calculate the sum of digits
#             return (
#                 1
#                 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj)
#                 + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)
#             )

#         visited = set()
#         return dfs(0, 0, 0, 0)


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i, j):
            # 无效情形1：机器人走出界了
            if i >= m or j >= n:
                return 0
            # 无效情形2：机器人走到一个之前访问过的（因为已经访问过了，所以对于结果‘能够到达多少格子’不能再算一次了）
            if (i, j) in visited:
                return 0
            # 无效情形3：数位之和>k了
            sum_i = i // 10 + i % 10  # 求出i的数位和（因为题目已经限制了0<=i<=99，所以只要除数为10即可）。下同
            sum_j = j // 10 + j % 10
            if sum_i + sum_j > k:  # 总的数位和
                return 0

            visited.add((i, j))  # 每次的有效情形都需要把坐标记录到已访问数组内
            # we can choose to go up or left, but we don't need to go back
            # if add  + dfs(i - 1, j) + dfs(i, j - 1)
            # we need to consider i,j < 0 and sometimes the (0,0) will be counted twice
            return 1 + dfs(i + 1, j) + dfs(i, j + 1)  # 此次dfs只需向下走或向右走，无需向上或向左（因为向上或向左意味着走回头路，而我之前只要
            # 判断过那个格子，满足的就是满足的，不满足的就是不满足的，没必要再来一遍）

        visited = set()
        res = dfs(0, 0)
        return res


# BFS
# the main difference between DFS and BFS is that BEF use the queue to store the next step


# class Solution:
#     def movingCount(self, m: int, n: int, k: int) -> int:
#         queue, visited = [(0, 0, 0, 0)], set()
#         while queue:
#             i, j, si, sj = queue.pop(0)
#             if i >= m or j >= n or k < si + sj or (i, j) in visited:
#                 continue
#             visited.add((i, j))
#             queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))
#             queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))
#         return len(visited)

if __name__ == "__main__":
    test = Solution()
    print(test.movingCount(2, 3, 1))
