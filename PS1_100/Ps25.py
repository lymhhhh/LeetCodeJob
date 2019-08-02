'''
25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def print(self):
        n = self.next
        print(self.val, end="")
        while n is not None:
            print("->" + str(n.val), end="")
            n = n.next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        t = 0
        ptr = head
        result = head
        if k == 1:
            return head
        elif k == 2:
            last = None
            while ptr is not None:
                if ptr.next is None:  # 判断是否需要reserve
                    if last is not None:
                        last.next = ptr
                    return result
                third = ptr.next.next
                ptr.next.next = ptr
                if last is not None:  # 判断是否是第一个逆转序列
                    last.next = ptr.next
                else:
                    result = ptr.next
                ptr.next = None
                last = ptr
                ptr = third
        # k>2时
        last = None
        while ptr is not None:
            p = ptr
            t = 0
            while p is not None and t < k:    # 判断是否需要reserve
                p = p.next
                t += 1
            if t < k:   # 不需要reserve
                if last is not None:
                    last.next = ptr
                return result
            # reserve
            t = 0
            l = ptr
            c = ptr.next
            third = None
            while t < k-1:
                third = c.next
                c.next = l
                l = c
                c = third
                t += 1

            if last is not None:  # 判断是否是第一个逆转序列
                last.next = l
            else:
                result = l

            # 修改状态
            ptr.next = None
            last = ptr
            ptr = c

        return result


head = ListNode(x=1)
head.next = ListNode(x=2)
head.next.next = ListNode(x=3)
head.next.next.next = ListNode(x=4)
head.next.next.next.next = ListNode(x=5)
head.next.next.next.next.next = ListNode(x=6)
head.next.next.next.next.next.next = ListNode(x=7)
sol = Solution()
sol.reverseKGroup(head, 3).print()

'''
网址：https://leetcode.com/problems/reverse-nodes-in-k-group/

最初思路：
1、判断序列长度是否需要reserve
2、reserve一个序列
3、将上一个序列的最终节点的next续到这个序列的开头
4、循环2,3

存在问题：无

参考思路：无

最终思路：无

改进方向：尚未思考

反思与总结：画图思考

'''