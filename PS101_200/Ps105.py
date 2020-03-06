'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def PreOrder(self):
        return [self.val,
                None if self.left is None else self.left.PreOrder(),
                None if self.left is None else self.right.PreOrder()]


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.divide(preorder, inorder)

    def divide(self, preorder, inorder):
        if len(preorder) <= 0:
            return None
        split = preorder[0]
        newRoot = TreeNode(split)

        splitIndex = inorder.index(split)

        leftInorder = inorder[0: splitIndex]
        rightInorder = inorder[splitIndex + 1: len(inorder)]

        leftPreorder = preorder[1 : splitIndex+1]
        rightPreorder = preorder[splitIndex+1: len(preorder)]

        leftTree = self.divide(leftPreorder, leftInorder)
        rightTree = self.divide(rightPreorder, rightInorder)

        newRoot.left = leftTree
        newRoot.right = rightTree

        return newRoot


s = Solution()

root = s.buildTree([3,9,20,15,7],
[9,3,15,20,7])
print(root.PreOrder())
