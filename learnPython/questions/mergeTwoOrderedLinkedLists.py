'''
Given two linked lists that are ordered in a non deacreasing manner, merge them to a single
linked list
'''

# Definition for singly-linked list.
from typing import List


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2


def print_linked_list(l) -> None:
    while l.next is not None:
        print(str(l.val) + "-->", end ="")
        l = l.next

    print(str(l.val) + "-->NULL", end="")

l1_n3 = ListNode(3, None)
l1_n2 = ListNode(2, l1_n3)
l1_n1 = ListNode(1, l1_n2)
l1 = [l1_n1, l1_n2, l1_n3]
print("list 1 is:\n")
print_linked_list(l1_n1)

l2_n3 = ListNode(4, None)
l2_n2 = ListNode(3, l2_n3)
l2_n1 = ListNode(1, l2_n2)
l2 = [l2_n1, l2_n2, l2_n3]
print("\n list 2 is:\n")
print_linked_list(l2_n1)


merged_list = merge_two_lists(l1_n1, l2_n1)
print("the merged list is:\n")
print_linked_list(merged_list)
