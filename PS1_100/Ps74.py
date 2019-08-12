'''
74. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        if matrix[0][0] == target:
            return True
        lline = 0
        rline = len(matrix)
        while rline - lline > 1:
            line = (lline + rline) // 2
            if matrix[line][0] > target:
                rline = line
            elif matrix[line][0] == target:
                return True
            else:
                lline = line

        line = lline
        lpoint = 0
        rpoint = len(matrix[line])
        while rpoint - lpoint > 1:
            point = (lpoint + rpoint) // 2
            if matrix[line][point] > target:
                rpoint = point
            elif matrix[line][point] == target:
                return True
            else:
                lpoint = point

        return False


sol = Solution()
print(sol.searchMatrix([[]], 3))
