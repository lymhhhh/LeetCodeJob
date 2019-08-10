'''
73. Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''


class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        flagi = False
        flagj = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and j == 0:
                    j += 1
                    continue
                if i == 0 and matrix[i][j] == 0:
                    flagi = True
                    continue
                if j == 0 and matrix[i][j] == 0:
                    flagj = True
                    continue
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(len(matrix) - 1, 0, -1):
            for j in range(len(matrix[0]) - 1, 0, -1):
                if i == 0 and j == 0:
                    break
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
            return
        if flagi:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if flagj:
            for i in range(len(matrix)):
                matrix[i][0] = 0


sol = Solution()
sol.setZeroes([[0, 2, 1, 4, 4],
               [1, 0, 1, 1, 1],
               [2, 3, 3, 3, 1],
               [0, 1, 1, 1, 1]])
sol.setZeroes([[1, 1, 1], [0, 1, 2]])
sol.setZeroes([[1, 0, 1]])
'''
标题：

网址：

内容：

最初思路：

存在问题：

参考思路：把每第一行和每第一列作为标志位，如果后面的值为0相关列和行置位标志位0

最终思路：

改进方向：忽略首列进行循环

代码：
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j]  == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well
        if is_col:
            for i in range(R):
                matrix[i][0] = 0
反思与总结：
'''

