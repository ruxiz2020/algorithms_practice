'''Given a linked list, rotate the list to the right by k places, where k is non-negative.'''

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
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0:
            return head
        if head == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        count = 0
        while p.next:
            p = p.next
            count += 1
        p.next = dummy.next
        step = count - ( k % count )
        for i in range(0, step):
            p = p.next
        head = p.next
        p.next = None
        return head


ss = Solution()
head = [1,2,3,4,5]
k = 2
ln_head = list_to_link(head)

res = ss.rotateRight(ln_head, k)
print('=== Given linked list : {}'.format(head))
print('=== Given k : {}'.format(k))
print('=== result is : {}'.format(link_to_list(res)))
