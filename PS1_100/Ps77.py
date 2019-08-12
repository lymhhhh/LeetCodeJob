'''
77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''


class Solution:
    def combine(self, n: int, k: int):
        set = [True] * n
        r = []
        for i in range(n):
            newset = set.copy()
            newset[i] = False
            current = [i + 1] + [0] * (k - 1)
            self.__f(r, current, newset, 1)
        return r

    # 把置为 ， 然后把传入 ，返回result
    def __f(self, r, current, set, k):
        if k >= len(current):
            r.append(current)
            return
        for i in range(current[k - 1], len(set)):
            if set[i]:
                newset = set.copy()
                newset[i] = False
                newcur = current.copy()
                newcur[k] = i + 1
                self.__f(r, newcur, newset, k + 1)


sol = Solution()
result = sol.combine(4, 2)
for l in result:
    print(l)
