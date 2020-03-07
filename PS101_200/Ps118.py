'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        result = [[1]]
        for row in range(1, numRows):
            result.append([1])
            for index in range(1, row):
                result[row].append(result[row - 1][index - 1] + result[row - 1][index])
            result[row].append(1)
        return result


print(Solution().generate(0))
