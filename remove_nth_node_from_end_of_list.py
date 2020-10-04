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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        root = ListNode(0)
        root.next = head #corner case when deleting head

        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return root.next

ss = Solution()
head = [1,2,3,4,5]
n = 2
ln_head = list_to_link(head)

res = ss.removeNthFromEnd(ln_head, n)
print('=== Given linked list : {}'.format(head))
print('=== and n : {}'.format(n))
print('=== result is : {}'.format(link_to_list(res)))
