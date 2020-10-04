
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

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2

        head = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return head.next


ss = Solution()
l1 = [1,2,4]
l2 = [1,3,4]
n1 = list_to_link(l1)
n2 = list_to_link(l2)

res = ss.mergeTwoLists(n1, n2)
print('=== Given 2 linked list : {} and {}'.format(l1, l2))
print('=== result is : {}'.format(link_to_list(res)))
