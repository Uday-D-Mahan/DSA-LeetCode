# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr.next:
            prev = curr
            curr = curr.next
            gcd_value = gcd(prev.val , curr.val)
            g = ListNode(gcd_value)
            prev.next = g
            g.next = curr
            

        return head