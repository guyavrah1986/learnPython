
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prev_overflow = 0
        # valid casue lists are non-empty
        l1_pointer = l1
        l2_pointer = l2
        print("l1.val is:" + str(l1_pointer.val) + " and l2.val is:" + str(l2_pointer.val))
        curr_val = l1_pointer.val + l2_pointer.val + prev_overflow
        if curr_val > 9:
            prev_overflow = 1
            print("over flow exists, cause curr value is originally:" + str(curr_val))
            curr_val -= 10

        ret_list_head = ListNode(curr_val, None)
        l1_pointer = l1_pointer.next
        l2_pointer = l2_pointer.next
        prev_node = ret_list_head
        while l1_pointer is not None or l2_pointer is not None:

            curr_val = prev_overflow
            if l1_pointer is not None:
                curr_val += l1_pointer.val
                print("l1.val is:" + str(l1_pointer.val))

            if l2_pointer is not None:
                curr_val += l2_pointer.val
                print("l2.val is:" + str(l2_pointer.val))

            if curr_val > 9:
                prev_overflow = 1
                print("over flow exists, cause curr value is originally:" + str(curr_val))
                curr_val -= 10
            else:
                prev_overflow = 0

            new_node = ListNode(curr_val, None)
            prev_node.next = new_node
            prev_node = new_node
            if l1_pointer is not None:
                l1_pointer = l1_pointer.next

            if l2_pointer is not None:
                l2_pointer = l2_pointer.next

        # if after the entire list we still have overflow, this is an "additional" edge case
        if prev_overflow > 0:
            new_node = ListNode(prev_overflow, None)
            prev_node.next = new_node

        return ret_list_head