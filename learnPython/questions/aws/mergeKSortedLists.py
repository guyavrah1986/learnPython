'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + "-->"


def merge_k_sorted_lists(lists: list) -> ListNode:
    if lists is None or not lists:
        return None

    k = len(lists)
    print("there are " + str(k) + " lists")
    # 1) get the heads of all lists
    curr_heads_list = []
    for i in range(k):
        curr_heads_list.append(lists[i][0])

    print("the heads of the " + str(k) + " lists are:")
    for head in curr_heads_list:
        print(head, end="")

    print("NULL")

    ret_list = []
    iter_num = 0
    while curr_heads_list:
        iter_num += 1
        curr_min_head = curr_heads_list[0]
        curr_min_head_index_in_list = 0
        num_of_heads = len(curr_heads_list)
        for i in range(1, num_of_heads):
            if curr_heads_list[i].val < curr_min_head.val:
                curr_min_head = curr_heads_list[i]
                curr_min_head_index_in_list = i

        if len(ret_list) > 0:
            # set the next filed of the current last element of the list to be the
            # node that is about to be added
            ret_list[-1].next = curr_min_head

        # now we have the current "min head", which is by the problem definition
        # the minimum elements amongst all list, so append it to the final list
        ret_list.append(curr_min_head)



        # if the next field of the curr_min_head is None, than it means that we are "done"
        # with this list, otherwise, overwrite this "list's head" with the next value of the
        # curr_min_head
        if curr_min_head.next is None:
            curr_heads_list.pop(curr_min_head_index_in_list)
        else:
            curr_heads_list[curr_min_head_index_in_list] = curr_min_head.next

        print("after iteration:" + str(iter_num) + ", the heads of the " + str(k) + " lists are:")
        for head in curr_heads_list:
            print(head, end="")

        print("NULL")

    return ret_list[0]


item3_list_1 = ListNode(5, None)
item2_list_1 = ListNode(4, item3_list_1)
item1_list_1 = ListNode(1, item2_list_1)
list_1 = [item1_list_1, item2_list_1, item3_list_1]

item3_list_2 = ListNode(4, None)
item2_list_2 = ListNode(3, item3_list_2)
item1_list_2 = ListNode(1, item2_list_2)
list_2 = [item1_list_2, item2_list_2, item3_list_2]


item2_list_3 = ListNode(6, None)
item1_list_3 = ListNode(2, item2_list_3)
list_3 = [item1_list_3, item2_list_3]

#lists = [[1,4,5],[1,3,4],[2,6]]
lists = [list_1, list_2, list_3]
expected_output = [1,1,2,3,4,4,5,6]
ret_val = merge_k_sorted_lists(lists)
tmp_head = ret_val
print("the returned list is:")
while tmp_head is not None:
    print(tmp_head, end="")
    tmp_head = tmp_head.next

print("NULL")

if ret_val != expected_output:
    print("got sorted list:" + str(ret_val) + ", BUT expected it to be:" + str(expected_output))
    exit(1)

