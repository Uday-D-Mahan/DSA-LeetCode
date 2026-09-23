class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        curr = head.next
        total = 0

        dummy = ListNode(0)
        result = dummy

        while curr:
            if curr.val == 0:
                if total != 0:
                    result.next = ListNode(total)
                    result = result.next
                    total = 0
            else:
                total += curr.val

            curr = curr.next

        return dummy.next
        