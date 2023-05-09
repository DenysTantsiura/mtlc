# 21. Merge Two Sorted Lists
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slist1 = slist2 = None
        if list1:
            slist1 = [list1.val]
            current_val1 = list1.next
            while current_val1 is not None:
                slist1.append(current_val1.val)
                current_val1 = current_val1.next

        if list2:
            slist2 = [list2.val]
            current_val2 = list2.next
            while current_val2 is not None:
                slist2.append(current_val2.val)
                current_val2 = current_val2.next

        slist1 = slist1 or []
        slist2 = slist2 or []
        result = slist1 + slist2
        result.sort()
        rez = None
        while len(result) != 0:
            rez = ListNode(result.pop(), rez)

        return rez
    
'''
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
'''
list1 = [1,2,4]
list2 = [1,3,4]
li1 = None
while len(list1) > 0:
    li1 = ListNode(list1.pop(), li1)

li2 = None
while len(list2) > 0:
    li2 = ListNode(list2.pop(), li2)

# while li1.next is not None:
#     print(li1.val)
#     li1 = li1.next
# print(li1.val)

# while li2.next is not None:
#     print(li2.val)
#     li2 = li2.next
# print(li1.val)

solution = Solution()

print(el:=solution.mergeTwoLists(li1, li2))  # +
while el.next:
    print(el.val)
    el = el.next

print(el.val)


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 or not list2:
            return list1 or list2
        
        if list2.val > list1.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
    

# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         if not list1 or not list2:
#             return list1 or list2
        
#         rez = None
#         if list1.next is None and list2.next is None:
#             rez = ListNode(list2.val, rez) if list1.val < list2.val else ListNode(list1.val, rez)
#             rez = ListNode(list1.val, rez) if list1.val < list2.val else ListNode(list2.val, rez)
#             return rez

#         while list1 and list2 and (list1.next or list2.next):  # list1 or list2:  # list1.next or list2.next:
#             if (list1.val is None) or (list1.val > list2.val):
#                 rez = ListNode(list2.val, rez)
#                 list2 = list2.next

#             elif (list2.next is None) or (list2.val >= list1.val):
#                 rez = ListNode(list1.val, rez)
#                 list1 = list1.next

#         if list1 and list2 and list1.next is None and list2.next is None:
#             rez = ListNode(list2.val, rez) if list1.val > list2.val else ListNode(list1.val, rez)
#             rez = ListNode(list1.val, rez) if list1.val > list2.val else ListNode(list2.val, rez)
        
#         if list1 is None or list1.next is None:
#             list1 = None

#         if  list2 is None or list2.next is None:
#             list2 = None

#         result = None
#         while rez.val:
#             result = ListNode(rez.val, result)
#             rez = rez.next
#             if rez is None:
#                 break

#         while list1:
#             result = ListNode(list1.val, result)
#             list1 = list1.next

#         while list2:
#             result = ListNode(list2.val, result)
#             list2 = list2.next

#         return result


# solution = Solution()

# li1 = ListNode(2)
# li2 = ListNode(1)
# print(el:=solution.mergeTwoLists(li1, li2))  # +
# while el.next:
#     print(el.val)
#     el = el.next

# print(el.val)
