# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.

class Solution:
    
    # Merge two sorted lists
    def mergeTwo(self, l1, l2):
        dummy = ListNode(-1)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        # Attach remaining part
        if l1:
            curr.next = l1
        else:
            curr.next = l2

        return dummy.next

    # Divide & Conquer
    def mergeListsRecur(self, i, j, lists):
        if i == j:
            return lists[i]

        mid = i + (j - i) // 2

        left = self.mergeListsRecur(i, mid, lists)
        right = self.mergeListsRecur(mid + 1, j, lists)

        return self.mergeTwo(left, right)

    def mergeKLists(self, lists):
        if not lists:
            return None

        return self.mergeListsRecur(0, len(lists) - 1, lists)