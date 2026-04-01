# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # create a dummy node to handle edge cases (like reversing from head)
        dummy = ListNode(0)
        dummy.next = head

        # pointer to node just before the 'left' position
        leftPre = dummy
        curr = head

        # move leftPre and curr to (left-1) and left positions
        cnt = 0
        while cnt < left - 1:
            cnt += 1
            leftPre = leftPre.next
            curr = curr.next
        
        # mark the start of sublist to be reversed
        sublistHead = curr

        # reverse nodes between left and right
        prev = None
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # reconnect the reversed sublist with the main list
        leftPre.next = prev
        sublistHead.next = curr

        return dummy.next

# method using head
# class Solution:
#     def reverseBetween(self, head, left, right):
        
#         dummy = ListNode(0)
#         dummy.next = head

#         # move to node before 'left'
#         leftPre = dummy
#         for i in range(left - 1):
#             leftPre = leftPre.next
        
#         # start reversing using head insertion
#         curr = leftPre.next

#         for i in range(right - left):
#             temp = curr.next
#             curr.next = temp.next
#             temp.next = leftPre.next
#             leftPre.next = temp
        
#         return dummy.next