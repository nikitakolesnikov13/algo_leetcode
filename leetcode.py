"""Task https://leetcode.com/problems/reverse-linked-list/"""
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed = None
        while head:
            temp = head.next
            head.next = reversed
            reversed = head
            head = temp
        return reversed

