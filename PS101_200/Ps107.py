'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        self.getResult(root, result, 0)
        result.reverse()
        return result

    def getResult(self, current, result, level):
        if len(result)<=level:
            result.append([])
        result[level].append(current.val)
        if current.left is not None:
            self.getResult(current.left, result, level+1)
        if current.right is not None:
            self.getResult(current.right, result, level + 1)

root = TreeNode(3)
root_left = TreeNode(9)
root.left = root_left

root_right = TreeNode(20)
root_right_left = TreeNode(15)
root_right_right = TreeNode(7)
root.right = root_right
root_right.left = root_right_left
root_right.right = root_right_right

print(Solution().levelOrderBottom(root))