import heapq
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
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for node in lists:
            if node:
                heap.append((node.val, node))
        heapq.heapify(heap)
        head = ListNode(0);
        curr = head

        while heap:
            pop = heapq.heappop(heap)
            curr.next = ListNode(pop[0])
            curr = curr.next
            if pop[1].next:
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))
        return head.next

ss = Solution()
lists = [[1,4,5],[1,3,4],[2,6]]
ls_nodes = []
for l in lists:

    ln_head = list_to_link(l)
    ls_nodes.append(ln_head)

res = ss.mergeKLists(ls_nodes)
print('=== Given linked list : {}'.format(lists))
print('=== result is : {}'.format(link_to_list(res)))
