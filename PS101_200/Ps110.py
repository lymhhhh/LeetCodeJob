'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.



Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return False
        return self.f(root) > 0

    def f(self, tree):
        if tree is None:
            return 0
        leftheight = self.f(tree.left)
        rightheight = self.f(tree.right)
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:
            return -1
        else:
            return max(leftheight, rightheight) + 1


root = TreeNode(3)
root_left = TreeNode(9)
root.left = root_left

root_right = TreeNode(20)
root_right_left = TreeNode(15)
root_right_right = TreeNode(7)
root.right = root_right
root_right.left = root_right_left
root_right.right = root_right_right
root_right_right_right = TreeNode(8)
root_right_right.right = root_right_right_right

print(Solution().isBalanced(root))
