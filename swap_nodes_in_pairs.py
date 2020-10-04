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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        while head.next and head.next.next:
            n1, n2 = head.next, head.next.next
            n1.next = n2.next
            n2.next = n1
            head.next = n2
            head = n1
        return dummy.next

ss = Solution()
head = [1,2,3,4]

ln_head = list_to_link(head)

res = ss.swapPairs(ln_head)
print('=== Given linked list : {}'.format(head))
print('=== result is : {}'.format(link_to_list(res)))
