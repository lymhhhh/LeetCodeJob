'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        _, m, maxNode = self.maxSum(root)
        if maxNode >= 0:
            return m
        else:
            return maxNode

    def maxSum(self, node):
        if node.left is None:
            left, leftmax, leftMaxNode = 0, 0, node.val
        else:
            left, leftmax, leftMaxNode = self.maxSum(node.left)

        if node.right is None:
            right, rightmax, rightMaxNode = 0, 0, node.val
        else:
            right, rightmax, rightMaxNode = self.maxSum(node.right)\

        return max([node.val + right, node.val + left, node.val]), \
               max([leftmax, rightmax, node.val + left + right, node.val + right, node.val + left, node.val]), \
               max([node.val, leftMaxNode, rightMaxNode])


root = TreeNode(2)
root_left = TreeNode(-1)
root_right = TreeNode(-2)
root_left_left = TreeNode(3)

root.left = root_left
root.right = root_right
#root_left.left = root_left_left

print(Solution().maxPathSum(root))
