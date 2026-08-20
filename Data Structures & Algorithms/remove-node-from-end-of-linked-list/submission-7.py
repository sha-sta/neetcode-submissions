# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        # if empty
        if not head:
            return head
        # if len 1
        if not head.next:
            return None
        # space it out
        for i in range(n):
            end = end.next
            if not end:
                return head.next
        remove = head
        while end.next:
            end = end.next
            remove = remove.next
        remove.next = remove.next.next
        return head