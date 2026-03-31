# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # apporach-1
        # make function of (reverse the LL)
        # then delete the (n - 1) position in LL
        # again reverse it 

        # approach - 2 (fast and slow)
        slow, fast = head, head
        
        # move fast n step ahead
        for i in range(n):
            fast = fast.next

        # remove head
        if fast is None:
            return head.next;

        # now move both pointer
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        # delete that node
        slow.next = slow.next.next

        return head
        