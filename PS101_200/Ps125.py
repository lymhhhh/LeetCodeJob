'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return False
        ss = list(s)
        uplist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
        sublist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        strings = []
        for word in ss:
            if self.getIndex(sublist, word) >= 0:
                strings.append(word)
            else:
                i = self.getIndex(uplist, word)
                if i >= 0:
                    strings.append(sublist[i])

        # print(strings)

        for i in range(len(strings) // 2):
            # print(strings[i],strings[len(strings)-i-1])
            if strings[i] != strings[len(strings) - i - 1]:
                return False
        return True

    def getIndex(self, l, o):
        for i in range(len(l)):
            if l[i] == o:
                return i
        return -1


print(Solution().isPalindrome("0P"))
