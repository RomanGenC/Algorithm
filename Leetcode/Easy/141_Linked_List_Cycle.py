# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        heads_values = {}
        while head and head.next:
            if heads_values.get(head.next):
                return True

            heads_values[head.next] = True
            head = head.next

        return False
