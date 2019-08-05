'''
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

import numpy as np


class Solution:
    def __split(self, num: str) -> list:
        i = len(num)
        result = []
        while i >= 5:
            result = [int(num[i - 5:i])] + result
            i -= 5
        if i > 0:
            result = [int(num[0:i])] + result
        return result

    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) >= len(num2):
            num1list = self.__split(num1)
            num2list = self.__split(num2)
        else:
            num1list = self.__split(num2)
            num2list = self.__split(num1)

        length = len(num1list) * len(num2list) + 2
        reslist = np.array([0] * length)
        templist = np.array([0] * length)

        j = len(num2list) - 1
        while j >= 0:
            mul = num2list[j]
            add = 0
            i = len(num1list) - 1
            templist = np.array([0] * length)
            while i >= 0:
                r = num1list[i] * mul + add
                # print(r, (len(num1list) - i - 1) + (len(num2list) - j - 1),r // 100000, r % 100000,)
                add = r // 100000
                templist[length - (len(num1list) - i - 1) - (len(num2list) - j - 1) - 1] = r % 100000
                i -= 1
            templist[length - (len(num1list) - i - 1) - (len(num2list) - j - 1) - 1] = add
            # print()
            # reslist += templist
            k = length - 1
            add = 0
            while k >= 0:
                r = reslist[k] + templist[k] + add
                add = r // 100000
                reslist[k] = r % 100000
                k -= 1
            j -= 1
            # print(templist)
            # print(reslist)
            # print("========================")
        i = length - 1
        flag = True
        result = ""
        for i in reslist:
            if flag:
                if i != 0:
                    flag = False
                    result = str(i)
            else:
                result += str(i).zfill(5)
        if flag:
            return "0"
        return result


sol = Solution()
print(sol.multiply(
    "140",
    "721"
))

'''

网址：https://leetcode.com/problems/multiply-strings/

最初思路：类似乘法算式一位位相乘，然后累加，可以改进为多位相乘

存在问题：慢

参考思路：

最终思路：

改进方向：

代码：

反思与总结：
'''
