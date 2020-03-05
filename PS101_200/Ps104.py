'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.nextLayer(root, 1)

    def nextLayer(self, tree, depth):
        if tree.left is None and tree.right is None:
            return depth
        if tree.left is None:
            return self.nextLayer(tree.right, depth+1)
        if tree.right is None:
            return self.nextLayer(tree.left, depth+1)
        return max(self.nextLayer(tree.left, depth+1), self.nextLayer(tree.right, depth+1))


a = TreeNode(1)

b = TreeNode(2)
b_left = TreeNode(4)
b_right = TreeNode(3)
b.left = b_left
# b.right = b_right

c = TreeNode(3)
c_left = TreeNode(4)
c_right = TreeNode(5)
# c.left = c_left
c.right = c_right

a.left = b
a.right = c

s = Solution()
print(s.maxDepth(a))
