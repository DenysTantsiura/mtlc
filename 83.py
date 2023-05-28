# https://leetcode.com/problemset/all/?status=NOT_STARTED&page=2
# 83. Remove Duplicates from Sorted List
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode(head.val) if head else None
        if not new:
            return new

        while head.next:
            if head.val != head.next.val:
                new = ListNode(head.next.val, new) 
            
            head = head.next

        head = ListNode(new.val)
        while new.next:
            new = new.next
            head = ListNode(new.val, head)

        return head


zero = ListNode(0)
for el in range(5):
    print(zero.val)
    zero = ListNode(el + (el%2), zero)
    if el == 2:
        print(zero.val)
        zero = ListNode(3, zero)

print(zero.val, '--------')

print(rez:=Solution().deleteDuplicates(zero))

while rez and rez.next:
    print(rez.val)
    rez = rez.next

print(rez.val)


"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previ = rez = ListNode(val=-1000,next=head)

        while head:
            if previ.val == head.val:
                previ.next = head.next

            else:
                previ = head

            head = head.next
        
        return rez.next
"""
