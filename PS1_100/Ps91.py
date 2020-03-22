'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
        dict = {'1': 'A',
                '2': 'B',
                '3': 'C',
                '4': 'D',
                '5': 'E',
                '6': 'F',
                '7': 'G',
                '8': 'H',
                '9': 'I',
                '10': 'J',
                '11': 'K',
                '12': 'L',
                '13': 'M',
                '14': 'N',
                '15': 'O',
                '16': 'P',
                '17': 'Q',
                '18': 'R',
                '19': 'S',
                '20': 'T',
                '21': 'U',
                '22': 'V',
                '23': 'W',
                '24': 'X',
                '25': 'Y',
                '26': 'Z'
                }
'''


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        sList = list(s)
        # change the number before 0 to #
        i = len(sList) - 1
        while i >= 0:
            if sList[i] == '0':
                sList.pop(i)
                sList[i] = '#'
            i -= 1
        print(sList)

        result = 1
        a1List = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        a2List = ['1', '2', '3', '4', '5', '6']
        z = 1
        y = 1
        x = 1
        # set start x,y,z

        #
        while i >= 0:
            if (sList[i] == 1 and sList[i + 1]) or \
                    (sList[i] == 2 and a2List.__contains__(sList[i + 1])):
                x = y + z
            else:
                x = y
            y = x
        return x


print(Solution().numDecodings("13789"))
