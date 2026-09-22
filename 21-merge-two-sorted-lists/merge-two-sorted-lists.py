# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        curr = list1

        if curr is None:
            list1 = list2
        else:
            while curr.next:
                curr = curr.next

            curr.next = list2

        value = []
        curr = list1

        while curr:
            value.append(curr.val)
            curr = curr.next

        value.sort()

        head = None
        tail = None

        for i in range(len(value)):
            new_node = ListNode(value[i])

            if head is None:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node

        return head
        