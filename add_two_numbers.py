#You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = l1
        b = l2
        root = None
        curNode = None
        carry = 0
        while a is not None or b is not None:
            if root is None:
                root = ListNode(a.val + b.val)
                curNode = root
            else:
                temp = None
                if a is not None and b is not None:
                    temp = ListNode(a.val + b.val + carry)
                elif a is not None:
                    temp = ListNode(a.val + carry)
                else:
                    temp = ListNode(b.val + carry)
                curNode.next = temp
                curNode = temp
                pass
            if curNode.val // 10 > 0:
                carry = curNode.val // 10
                curNode.val = curNode.val % 10
            else:
                carry = 0
            if a is not None:
                a = a.next
            if b is not None:
                b = b.next
        if carry > 0:
            temp = ListNode(carry)
            curNode.next = temp
        return root
    pass

li1 = ListNode(2)
li2 = ListNode(4)
li3 = ListNode(3)
li1.next = li2
li2.next = li3

li4 = ListNode(5)
li5 = ListNode(6)
li6 = ListNode(4)
li4.next = li5
li5.next = li6

li7 = Solution().addTwoNumbers(li1,li4)
print(li7)

li9 = ListNode(5)
li8 = Solution().addTwoNumbers(li9,li9)
print(li8)









        #a = l1
        #b = l2
        #root = None
        #isCarry = False
        #while a is not None or b is not None:
        #    if not isCarry:
        #        temp = None
        #        if a is not None and b is not None:
        #            temp = ListNode(a.val + b.val)
        #        elif a is not None:
        #            temp = ListNode(a.val)
        #        else:
        #            temp = ListNode(b.val)
        #        temp.next = root
        #        root = temp
        #    else:
        #        if a is not None and b is not None:
        #            root.val += a.val + b.val
        #        elif a is not None:
        #            root.val += a.val
        #        else:
        #            root.val += b.val
        #    if root.val // 10 > 0:
        #        isCarry = True
        #        temp = ListNode(root.val // 10)
        #        temp.next = root
        #        root.val = root.val % 10
        #        root = temp
        #    else:
        #        isCarry = False
        #    if a is not None:
        #        a = a.next
        #    if b is not None:
        #        b = b.next
        #temp = None
        #while root.next is not None:
        #    x = root.next
        #    root.next = temp
        #    temp = root
        #    root = x
        #root.next = temp