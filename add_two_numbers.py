'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_link(lst):
    """Takes a Python list and returns a Link with the same elements.
    """
    if len(lst) == 1:
        return ListNode(lst[0])
    return ListNode(lst[0], list_to_link(lst[1:]))  # <<<< RECURSIVE


def link_to_list(ln):
    ls = []
    while ln.val!= None:
        ls.append(ln.val)
        if ln.next!=None:
            ln = ln.next
        else:
            return ls


def next_ll(state=['a']):
    value = state[0]
    if value is not None:
        state[0] = child[value]
        return value


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s = 0
        dummy = ListNode(0)
        tail = dummy
        while l1 or l2 or s > 0:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            tail.next = ListNode(s % 10)
            s //= 10
            tail = tail.next
        return dummy.next


ss = Solution()
l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
ln1 = list_to_link(l1)
ln2 = list_to_link(l2)
res = ss.addTwoNumbers(ln1, ln2)
print('=== Given  : {}'.format(l1))
print('=== and  : {}'.format(l2))
print('=== result is : {}'.format(link_to_list(res)))
