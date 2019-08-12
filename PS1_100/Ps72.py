'''
72. Edit Distance

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1 = list(word1)
        w2 = list(word2)
        if len(w1) == 0:
            return len(w2)
        if len(w2) == 0:
            return len(w1)
        map1 = [0] * len(w2)
        map2 = [0] * len(w2)

        for j in range(0, len(w2)):
            if w1[0] == w2[j]:
                map1[j] = max(map1[j-1], j)
            else:
                map1[j] = map1[j-1]+1
        print(map1)
        for i in range(1, len(w1)):
            if w1[i] == w2[0]:
                map2[0] = max(map1[0], i)
            else:
                map2[0] = map1[0] + 1
            for j in range(1, len(w2)):
                if w1[i] == w2[j]:
                    map2[j] = map1[j-1]
                else:
                    map2[j] = min(map1[j], map2[j-1], map1[j-1])+1
            map1 = map2
            map2 = [0] * len(w2)
            #print(i,"\t",map1, w1[i])

        return map1[len(w2)-1]


sol = Solution()
print(sol.minDistance("a", "a"))
print("///////////////////////////////////////////////////////////")
print(sol.minDistance("horse", "ros"))
print("///////////////////////////////////////////////////////////")
print(sol.minDistance("intention", "execution"))
print("///////////////////////////////////////////////////////////")
print(sol.minDistance("mart", "karma"))
#print("///////////////////////////////////////////////////////////")
#print(sol.minDistance("spartan", "part"))
#print("///////////////////////////////////////////////////////////")
#print(sol.minDistance("sea", "ate"))
print("///////////////////////////////////////////////////////////")
print(sol.minDistance("xuxux", "uy"))