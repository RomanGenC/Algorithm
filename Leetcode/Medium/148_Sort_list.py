# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        sort_list = head
        while sort_list:
            values.append(sort_list.val)
            sort_list = sort_list.next

        values.sort()

        change_values = head
        for i in values:
            change_values.val = i
            change_values = change_values.next

        return head
