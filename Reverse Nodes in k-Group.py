# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverse(self, head,k):
        newHead = None
        li = [head]
        i = 1
        while head.next != None and i < k:
            head = head.next
            li.append(head)
            i+=1
        while len(li) > 0:
            x = li.pop()
            if newHead == None:
                newHead = x
            if len(li) > 0:
                x.next = li[-1]
            else:
                x.next = None
        return newHead,i

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or k == 1:
            return head
        
        newHead = None
        cur = head
        lastTail = None
        while cur != None:
            temp = cur
            for i in range(k):
                if temp.next != None:
                    temp = temp.next
                else: break
            if i + 1 != k:
                if lastTail == None:
                    return head
                lastTail.next = cur
                return newHead
            temp2,x = self.reverse(cur,k)
            if newHead == None:
                newHead = temp2
            else:
                lastTail.next = temp2
            lastTail = cur
            if x != k or cur == temp or temp == temp2:
                break
            cur = temp
        lastTail.next = None
        return newHead

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
x = Solution().reverseKGroup(n1,3)

x = Solution().reverseKGroup(None,5)
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
x = Solution().reverseKGroup(n1,5)

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
x = Solution().reverseKGroup(n1,2)

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
x = Solution().reverseKGroup(n1,3)

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
x = Solution().reverseKGroup(n1,4)

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
x = Solution().reverseKGroup(n1,6)

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
x = Solution().reverseKGroup(n1,1)