"""Task - 206. Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/"""
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


############################################################################################
"""Task - 876. Middle of the Linked List - https://leetcode.com/problems/reverse-linked-list/"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
