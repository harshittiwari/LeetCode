# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def findPosition(self, x, lists):
        lo = 0
        hi = len(lists)
        while lo < hi:
            mid = (lo+hi)//2
            if lists[mid].val < x.val: lo = mid+1
            else: hi = mid
        return lo

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        root = None
        cur = None
        lists = [x for x in lists if x is not None]
        lists.sort(key=lambda x: x.val)
        while len(lists) > 0:
            if root == None:
                root = lists[0]
                cur = root
            else:
                cur.next = lists[0]
                cur = cur.next
            if lists[0].next == None:
                lists.pop(0)
            else:
                if len(lists) == 1:
                    lists[0] = lists[0].next
                else:
                    x = lists[0].next
                    lists.pop(0)
                    lists.insert(self.findPosition(x,lists),x)
                pass
        return root

n1 = ListNode(3)
n2 = ListNode(5)
n1.next = n2
n3 = ListNode(6)
n2.next = n3
n4 = ListNode(7)
n3.next = n4

n5 = ListNode(3)
n6 = ListNode(4)
n5.next = n6
n7 = ListNode(8)
n6.next = n7

n8 = ListNode(0)
n9 = ListNode(1)
n8.next = n9
n10 = ListNode(2)
n9.next = n10

print(Solution().mergeKLists([n1,n5,n8]))
print(Solution().mergeKLists([None,None]))