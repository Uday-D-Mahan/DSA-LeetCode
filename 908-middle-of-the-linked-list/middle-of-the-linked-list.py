# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next

        middle = count // 2

        curr = head

        for i in range(middle):
            curr = curr.next

        return curr