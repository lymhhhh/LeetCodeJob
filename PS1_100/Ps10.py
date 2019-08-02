'''
10. Regular Expression Matching

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        A = list(s)
        blist = list(p)
        letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z',
                   'x', 'c', 'v', 'b', 'n', 'm', '.']
        # Special Case: the length of s or p is 0
        if len(A) == 0:
            if len(blist) == 0:
                return True
            else:
                if len(blist)%2 == 0:
                    for i in range(len(blist)//2):
                        if not(blist[i*2+1]=='*' and blist[i*2] in letters):
                            return False
                    return True
                return False
        else:
            if len(blist) == 0:
                return False
        if blist[0] == '*':
            return False
        # Normal Case
        a = 0
        b = 0
        t = 0
        B = []
        Bstates = []

        while b < len(blist):
            if blist[b] in letters and b + 1 < len(blist) and blist[b + 1] == '*':
                B.append(blist[b])
                Bstates.append(True)
                b += 1
            elif blist[b] == '*':
                return False
            else:
                B.append(blist[b])
                Bstates.append(False)
                t += 1
            b += 1
        if t>len(A):
            return False
        b = 0
        next = 0
        #print(B, Bstates)
        states1 = [0] * len(A)
        states2 = [0] * len(A)
        #print(states1)
        while b < len(B):
            flag = True
            while a < len(A):
                if (B[b] == A[a] or B[b] == '.') and not Bstates[b]:
                    if flag:
                        next = a
                    flag = False
                    if a == 0:
                        states2[a] = 1
                    else:
                        states2[a] = states1[a - 1] + 1
                elif (B[b] == A[a] or B[b] == '.') and Bstates[b]:
                    if flag:
                        next = a
                    flag = False
                    if a == 0:
                        states2[a] = 1
                    else:
                        states2[a] = max(states1[a - 1], states2[a - 1]) + 1
                        if B[b] == '.':
                            states2[a] = max(states2[a], states1[a])

                else:
                    if not Bstates[b]:
                        states2[a] = 0
                a += 1
            if flag and not Bstates[b]:
                #print(b, flag, not Bstates[b])
                return False
            print(B[b], states2)
            b += 1
            a = next
            states1 = states2.copy()

        if states1[len(A) - 1] == len(A):
            return True
        return False


solution = Solution()
print(solution.isMatch("baabbbaccbccacacc","c*..b*a*a.*a..*c"))
