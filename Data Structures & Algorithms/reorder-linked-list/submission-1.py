# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid
        mid = head
        fast = head
        while fast.next and fast.next.next:
            mid = mid.next
            fast = fast.next.next
        
        # reverse from mid to end
        second = self.reverseList(mid.next)
        mid.next = None
        
        # coalesce halves together
        first = head

        while second:
            f_next = first.next
            s_next = second.next
            first.next = second
            second.next = f_next
            first = f_next
            second = s_next