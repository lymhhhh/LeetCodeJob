'''
67. Add Binary
Easy

1071

202

Favorite

Share
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        state = 0
        result = []
        while i >= 0 and j >= 0:
            if a[i] == '1' and b[j] == '1':
                result = [state] + result
                state = 1
            elif a[i] == '0' and b[j] == '0':
                result = [state] + result
                state = 0
            elif state == 0:
                result = [1] + result
                state = 0
            elif state == 1:
                result = [0] + result
                state = 1
            i -= 1
            j -= 1
        while i >= 0:
            if a[i] == '1' and state == 1:
                result = [0] + result
                state = 1
            elif a[i] == '0' and state == 0:
                result = [0] + result
                state = 0
            else:
                result = [1] + result
                state = 0
            i -= 1
        while j >= 0:
            if b[j] == '1' and state == 1:
                result = [0] + result
                state = 1
            elif b[j] == '0' and state == 0:
                result = [0] + result
                state = 0
            else:
                result = [1] + result
                state = 0
            j -= 1
        if state == 1:
            result = [1] + result
        r = ""
        for i in range(len(result)):
            r += str(result[i])
        return r


sol = Solution()
print(sol.addBinary("100","110010"))
