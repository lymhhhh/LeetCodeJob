'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


Example 1:



Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000
'''


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        self.nextLevel(root)
        return root

    def nextLevel(self, root):
        if root.left is None:
            return
        root.left.next = root.right
        if root.next is not None:
            root.right.next = root.next.left
        self.nextLevel(root.left)
        self.nextLevel(root.right)


a = Node(1)

b = Node(2)
b_left = Node(4)
b_right = Node(5)
b.left = b_left
b.right = b_right

c = Node(3)
c_left = Node(6)
c_right = Node(7)
c.left = c_left
c.right = c_right

a.left = b
a.right = c

s = Solution()
a = s.connect(a)
print()
print(b_right.next.val, c_right.next)