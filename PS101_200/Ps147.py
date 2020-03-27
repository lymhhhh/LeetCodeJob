'''
Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list


Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def Iprint(self):
        c = self
        result = ""
        while c is not None:
            result = result + "," + str(c.val)
            c = c.next
        print(result)

    def create(self, l):
        head = ListNode(l[0])
        node = head
        i = 1
        while i < len(l):
            newNode = ListNode(l[i])
            node.next = newNode
            node = newNode
            i += 1
        return head


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        current = head.next
        last = head
        next = head.next.next

        flag = True


        while current is not None:
            #print("#####################################")
            #head.Iprint()
            #print(last.val, current.val, next.val)
            #print("#####################################")
            itr = head.next
            itrlast = head
            # head
            if itrlast.val > current.val:
                last.next = next
                current.next = itrlast
                head = current
                flag = False

            else:
                # mid
                while itr != next:
                    # print("-------------------------------------------------")
                    # print(last.val, current.val, itr.val, itrlast.val)
                    # head.Iprint()
                    # print("-------------------------------------------------")
                    # input()
                    if current.val < itr.val:
                        last.next = next
                        current.next = itr
                        itrlast.next = current
                        flag = False
                        break
                    itrlast = itr
                    itr = itr.next

            # update
            if flag:
                last = current
            current = next
            if current is None:
                return head
            next = current.next

            flag = True

        return head


head = ListNode(0).create([4,2,1,3])
head =  Solution().insertionSortList(head)
head.Iprint()
