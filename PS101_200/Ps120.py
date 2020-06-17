'''
120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''

import numpy as np

'''
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        map = np.zeros((len(triangle), len(triangle)), np.int16)
        map[0][0] = triangle[0][0]
        for i in range(1, len(triangle) - 1):
            # print(map)
            for j in range(1, i):
                map[i][j] = min(map[i - 1, j - 1], map[i - 1, j]) + triangle[i][j]
            map[i][0] = map[i - 1][0] + triangle[i][0]
            map[i][i] = map[i - 1][i - 1] + triangle[i][i]

        i = len(triangle) - 1
        if i>0:
            m = 10000000
            for j in range(1, i):
                map[i][j] = min(map[i - 1, j - 1], map[i - 1, j]) + triangle[i][j]
                if map[i][j] < m:
                    m = map[i][j]
            map[i][0] = map[i - 1][0] + triangle[i][0]
            if map[i][0] < m:
                m = map[i][0]
            map[i][i] = map[i - 1][i - 1] + triangle[i][i]
            if map[i][i] < m:
                m = map[i][i]

            # print(triangle)
            #print(map)
            return m
        else:
            return map[0][0]
'''

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = triangle[-1]
        print(dp)
        for i in range(len(triangle) - 2, -1, -1):
            tmp = [None for _ in range(i + 1)]
            for j in range(len(tmp)):
                tmp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
            print(tmp)
            dp = tmp
        return dp[0]

A = [
    [2],
    [3, 4],
    [6, 5, 1],
    [4, 1, 8, 3]
]
B = [[-10]]
print(Solution().minimumTotal(A))
#print(Solution().minimumTotal(B))

