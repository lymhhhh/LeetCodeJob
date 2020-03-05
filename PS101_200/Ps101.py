'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Note:
Bonus points if you could solve it both recursively and iteratively.

'''


# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.compare(root.left, root.right)

    def compare(self, a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False

        if a.val == b.val:
            return self.compare(a.left, b.right) and self.compare(a.right, b.left)
        return False


a = TreeNode(1)

b = TreeNode(2)
b_left = TreeNode(4)
b_right = TreeNode(3)
b.left = b_left
b.right = b_right

c = TreeNode(2)
c_left = TreeNode(4)
c_right = TreeNode(3)
c.left = c_left
c.right = c_right

a.left = b
a.right = c

s = Solution()
print(s.isSymmetric(None))

