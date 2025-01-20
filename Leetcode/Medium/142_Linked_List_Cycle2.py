# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import Optional


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        heads_values = {}
        while head:
            if heads_values.get(head):
                return head

            heads_values[head] = True
            head = head.next

        return None