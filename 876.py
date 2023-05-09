# 876. Middle of the Linked List
# Definition for singly-linked list.
from copy import deepcopy
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stop = 0
        el = head
        while el:
            stop += 1
            el = el.next
        stop = stop // 2
        while stop:
            stop -= 1
            head = head.next
        
        return head


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        simple_list = []
        
        while head:
            simple_list.append(head.val)
            head = head.next

        simple_list = simple_list[len(simple_list)//2:]

        while simple_list:
            head = ListNode(simple_list.pop(), head)
        
        return head
    

solution = Solution()

# print(solution.middleNode(...))  # +

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None
        stop = 0
        
        while head:
            stop += 1
            new_list = ListNode(head.val, new_list)
            head = head.next

        stop = round(stop / 2 + 0.2)

        while stop:
            stop -= 1
            head = ListNode(new_list.val, head)
            new_list = new_list.next
        
        return head
    

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rabbit = head

        while rabbit and rabbit.next:
            head = head.next
            rabbit = rabbit.next.next

        return head


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stop = 0
        el = head
        while el:
            stop += 1
            el = el.next
        stop = stop // 2
        [head := head.next for _ in range(stop)]
        
        return head
