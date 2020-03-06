'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def PreOrder(self):
        print(self.val)
        return [self.val,
                [None] if (self.left is None) else self.left.PreOrder(),
                [None] if (self.right is None) else self.right.PreOrder()]


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.ToTree(nums)

    def ToTree(self, nums):
        if len(nums) <= 0:
            return None
        split = int(len(nums) / 2)
        newTree = TreeNode(nums[split])
        newTree.left = self.ToTree(nums[0:split])
        newTree.right = self.ToTree(nums[split + 1:len(nums)])
        return newTree


tree = Solution().sortedArrayToBST([1, 2, 3, 4, 5])
print(tree.val, tree.left.val, tree.right.val)
print(tree.PreOrder())
