# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import random
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.depth = 1
        cur = self.head
        while cur.next != None:
            self.depth += 1
            cur = cur.next
        
    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        index = random.randint(1,self.depth)
        cur = self.head
        while index != 1:
            cur = cur.next
            index -= 1
        return cur

# Your Solution object will be instantiated and called as such:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
obj = Solution(head)
print(obj.getRandom().val)
print(obj.getRandom().val)
print(obj.getRandom().val)