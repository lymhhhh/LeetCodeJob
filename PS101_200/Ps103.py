'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.getResult(root, 0, result)
        return result

    def getResult(self, root, index, result):
        if root is None:
            return
        if len(result) == index:
            result.append([])

        if index % 2 == 0:
            result[index].append(root.val)
        else:
            result[index].insert(0, root.val)

        self.getResult(root.left, index + 1, result)
        self.getResult(root.right, index + 1, result)




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
print(s.zigzagLevelOrder(a))
