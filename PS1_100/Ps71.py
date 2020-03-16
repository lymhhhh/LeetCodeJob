'''
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system,
a period . refers to the current directory.
Furthermore, a double period .. moves the directory up a level.
For more information, see: Absolute path vs relative path in Linux/Unix

Note that the returned canonical path must always begin with a slash /,
and there must be only a single slash / between two directory names.
The last directory name (if it exists) must not end with a trailing /.
Also, the canonical path must be the shortest string representing the absolute path.



Example 1:

Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
Example 4:

Input: "/a/./b/../../c/"
Output: "/c"
Example 5:

Input: "/a/../../b/../c//.//"
Output: "/c"
Example 6:

Input: "/a//b////c/d//././/.."
Output: "/a/b/c"
'''


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # change str to list, remove all "." and double "/"
        # example:
        # . // /// /./
        pathlist = path.split('/')
        pathlist = list(filter(lambda a: a != '' and a != '.', pathlist))
        #print(pathlist)

        result = ""
        up = 0
        resultlist = []
        for p in pathlist:
            if p == "..":
                if len(resultlist)>0:
                    resultlist.pop()
            else:
                resultlist.append(p)

        #print(resultlist)
        if len(resultlist) <= 0:
            return "/"
        for p in resultlist:
            result = result+'/'+p
        return result

print(Solution().simplifyPath("/.///NWtm/KBp/TQdj/a/v/rsJ/n/j/../../lsw/./j/../Gh/////gNBxM/./"))
