# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def reverse(self, head):
        curr = head
        prev = None
        next = None

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev


    def insertAtTail(self, head, tail, val):
        temp = ListNode(val)

        # if list is empty
        if head is None:
            head = temp
            tail = temp
            return head, tail
        else:
            # if list is non-empty
            tail.next = temp
            tail = temp
            return head, tail


    def addTwoNumbers(self, l1, l2):

        carry = 0

        ansHead = None
        ansTail = None

        # while l1 is not None and l2 is not None:

        #     total = carry + l1.val + l2.val

        #     digit = total % 10

        #     ansHead, ansTail = self.insertAtTail(ansHead, ansTail, digit)

        #     carry = total // 10

        #     l1 = l1.next
        #     l2 = l2.next
        
        # while l1 is not None:
        #     total = carry + l1.val

        #     digit = total % 10

        #     ansHead, ansTail = self.insertAtTail(ansHead, ansTail, digit)

        #     carry = total // 10

        #     l1 = l1.next

        # while l2 is not None:
        #     total = carry + l2.val
            
        #     digit = total % 10

        #     ansHead, ansTail = self.insertAtTail(ansHead, ansTail, digit)

        #     carry = total // 10

        #     l2 = l2.next
        
        # # handle remaining carry
        # if carry:
        #     ansHead, ansTail = self.insertAtTail(ansHead, ansTail, carry)

        # return ansHead

        while l1 is not None or l2 is not None or carry:

            val1 = 0
            if l1 is not None:
                val1 = l1.val
            
            val2 = 0
            if l2 is not None:
                val2 = l2.val

            sum = carry + val1 + val2

            digit = sum % 10

            ansHead, ansTail = self.insertAtTail(ansHead, ansTail, digit)

            carry = sum // 10

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next
        
        return ansHead
