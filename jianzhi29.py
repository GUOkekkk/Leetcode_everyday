from typing import List


# the key of this question is how to find the boundary of the matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # the special case
        if matrix == []:
            return []

        # the right and bottom boundary
        bottom = len(matrix)
        right = len(matrix[0])

        res = []
        # the left and top boundary
        top = 0
        left = 0

        # the bottom > the top and the right > the left
        while top < bottom and left < right:
            for k in range(left, right):
                res.append(matrix[top][k])
            top += 1
            for k in range(top, bottom):
                res.append(matrix[k][right - 1])
            right -= 1
            if top < bottom:
                # in range if range(5, -1, -1) would be [5, 4, 3, 2, 1, 0]
                for k in range(right - 1, left - 1, -1):
                    res.append(matrix[bottom - 1][k])
                bottom -= 1
            if left < right:
                for k in range(bottom - 1, top - 1, -1):
                    res.append(matrix[k][left])
                left += 1
        return res
