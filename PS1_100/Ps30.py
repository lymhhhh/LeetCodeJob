'''
30. Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
'''


class Solution:
    def findSubstring(self, s: str, words):
        if len(words) == 0:
            return []
        size = len(words[0])
        length = len(s) // size
        states = [-1] * length
        for i in range(length):
            for j in range(len(words)):
                if s[i * size:(i + 1) * size] == words[j]:
                    states[i] = j
        want = [0] * len(words)
        start = 0
        last = 0
        i = 0
        result = []
        print(states)
        while i < length:
            if states[i] > -1:
                want[states[i]] += 1
                if want[states[i]] == 2:
                    j = 0
                    while j < len(want):
                        if want[j] == 0:
                            want = [0] * len(want)
                            want[states[i]] += 1
                            break
                        j += 1
                    if j == len(words):
                        result.append(start)
                        i = start//size
                        start = start+size
                        want = [0] * len(want)
                    else:
                        start = size * i
            else:
                j = 0
                while j < len(want):
                    if want[j] == 0:
                        want = [0] * len(want)
                        want[states[i]] += 1
                        break
                    j += 1
                if j == len(words):
                    result.append(start)
                    start = size*(i+1)
                    want = [0] * len(want)
                else:
                    start = size * i
            i += 1
        j = 0
        for j in range(len(want)):
            if want[j] == 0:
                break
        if j == len(words)-1:
            result.append(start)
        return result


sol = Solution()
print(sol.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]))
