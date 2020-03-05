'''
79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''

import copy

class Solution:
    def exist(self, board, word: str) -> bool:
        w = list(word)
        for i in range(len(board)):
            for j in range(len((board[0]))):
                if w[0] == board[i][j]:  # DFS
                    q = [] # 栈
                    map = [[True]*len(board[0]) for a in range(len(board))]
                    map[i][j] = False
                    q.append([1, i, j])
                    while len(q) > 0:

        return False


sol = Solution()
print(sol.exist([["a","a","a"],
                 ["a","a","a"],
                 ["a","a","b"]],"aaaaaaaaaaaaaaaaaaaa"))
# []