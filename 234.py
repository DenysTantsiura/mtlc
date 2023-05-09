# 234. Palindrome Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        a, b, c = head, head, None

        while b and b.next:
            a, b = a.next, b.next.next
        c, a, c.next = a, a.next, None

        while a:
            a.next, c, a = c, a, a.next
        b, a = head, c

        while a:
            if b.val != a.val: 
                return False
            b, a = b.next, a.next

        return True
