'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false

'''


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        strings = list(s)
        patterns = list(p)
        return self.Compare(strings, patterns, 0, 0)

    def Compare(self, strings, parttens, sIndex, pIndex):
        #print("------", sIndex, pIndex)
        while sIndex < len(strings) and pIndex < len(parttens):
            #print(strings[sIndex] , parttens[pIndex])
            if strings[sIndex] == parttens[pIndex] or parttens[pIndex] == '?':
                sIndex += 1
                pIndex += 1
            elif parttens[pIndex] == '*':
                return (self.Compare(strings, parttens, sIndex + 1, pIndex)
                        or self.Compare(strings, parttens, sIndex + 1, pIndex + 1)
                        or self.Compare(strings, parttens, sIndex, pIndex + 1))
            else:
                return False
        while pIndex<len(parttens) and parttens[pIndex] == "*":
            pIndex += 1;
        if sIndex == len(strings) and pIndex == len(parttens):
            return True
        return False


print(Solution().isMatch("aaabababaaabaababbbaaaabbbbbbabbbbabbbabbaabbababab", "*ab***ba**b*b*aaab*b"))