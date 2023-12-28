# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = 0
        result = ListNode()
        current = result
        while l1 is not None or l2 is not None:
            var1 = l1.val if l1 else 0
            var2 = l2.val if l2 else 0

            total = var1 + var2 + temp

            temp = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if temp != 0:
            current.next = ListNode(temp)
            current = current.next
        return result.next