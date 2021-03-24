

class Node:

    def __init__(self, val: int):
        self.val = val
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_node: object):
        self._next = next_node


class LinkedList:

    def __init__(self):
        self._head = None

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, new_head):
        self._head = new_head

    def insert_element(self, new_node: Node):
        # empty list
        if self._head is None:
            self._head = new_node
            return

        # new_node is smaller than current head
        if self._head.val > new_node.val:
            new_node.next = self._head
            self._head = new_node
            return

        curr = self._head
        while curr.next is not None and curr.next.val < new_node.val:
            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node

    def print_list(self):
        tmp = self._head
        while tmp is not None:
            print(str(tmp.val) + "-->", end="")
            tmp = tmp.next

        print("NULL")


def add_node_to_list(list_head: Node, node_to_add: Node):
    print("about to add node with val:" + str(node_to_add.val))
    print("list head point to val:" + str(list_head.val))
    if list_head is None or node_to_add is None:
        return None

    orig_list_head = list_head
    print("setting the original list head to:" + str(orig_list_head.val))
    if list_head.val > node_to_add.val:
        print("new node:" + str(node_to_add.val) + " is about to be inserted as the new head")
        node_to_add.next = list_head
        list_head.prev = node_to_add
        return node_to_add

    '''
    if list_head.next is None:
        print("list_head.next is None")
        if list_head.val > node_to_add.val:
            print("inserting " + str(node_to_add.val) + " as the new head of the list")
            node_to_add.next = list_head
            list_head.prev = node_to_add
        else:
            list_head.next = node_to_add
            node_to_add.prev = list_head

        return node_to_add
    '''
    tmp_node = list_head
    while tmp_node is not None and tmp_node.val < node_to_add.val:
        print("passed node with val:" + str(tmp_node.val))
        tmp_node = tmp_node.next

    if tmp_node is None:
        print("about to insert node at the end of the list")
        tmp_node.next = node_to_add
        node_to_add.prev = tmp_node
    else:
        if tmp_node.val > node_to_add.val:
            print("inserting new node:" + str(node_to_add.val) + " BEFORE node:" + str(tmp_node.val))
            print("tmp_node.prev.val is:" + str(tmp_node.prev.val))

            node_to_add.next = tmp_node
            node_to_add.prev = tmp_node.prev
            node_to_add.prev.next = node_to_add
            print("node_to_add.next.val is:" + str(node_to_add.next.val))
            print("node_to_add.prev.val is:" + str(node_to_add.prev.val))
            print("node_to_add.prev.next.val is:" + str(node_to_add.prev.next.val))
            print("tmp_node.prev.val is:" + str(tmp_node.prev.val))
            #print("tmp_node.next.val is:" + str(tmp_node.next.val))
        else:
            print("inserting new node:" + str(node_to_add.val) + " AFTER node:" + str(tmp_node.val))

    return orig_list_head

'''
n1 = Node(17)
n2 = Node(9)
n3 = Node(12)
n4 = Node(10)
n5 = Node(8)
n6 = Node(11)
n7 = Node(15)
list_head = n1

# n1-->n2
n1.next = n2

# n1<--n2-->n3
n2.prev = n1
n2.next = n3

# n2<--n3-->n4
n3.prev = n2
n3.next = n4

# n3<--n4-->n5
n4.prev = n3
n4.next = n5


print("at the beginning the list is as follows:")
print_list(list_head)
list_head = add_node_to_list(list_head, n2)
print("after inserting n2 (" + str(n2.val) + "), the list is as follows:")
print("list_head.val is:" + str(list_head.val))
print_list(list_head)
list_head = add_node_to_list(list_head, n3)
print("after inserting n3 (" + str(n3.val) + "), the list is as follows:")
print("list_head.val is:" + str(list_head.val))
print_list(list_head)
list_head = add_node_to_list(list_head, n4)
print("after inserting n4 (" + str(n4.val) + "), the list is as follows:")
print("list_head.val is:" + str(list_head.val))
print_list(list_head)
list_head = add_node_to_list(list_head, n5)
print("after inserting n5 (" + str(n5.val) + "), the list is as follows:")
print("list_head.val is:" + str(list_head.val))
print_list(list_head)
list_head = add_node_to_list(list_head, n6)
print("after inserting n6 (" + str(n6.val) + "), the list is as follows:")
print("list_head.val is:" + str(list_head.val))
print_list(list_head)
list_head = add_node_to_list(list_head, n7)
print("after inserting n7 (" + str(n7.val) + "), the list is as follows:")
print("list_head.val is:" + str(list_head.val))
print_list(list_head)
'''

linked_list = LinkedList()
n1 = Node(5)
linked_list.insert_element(n1)
n2 = Node(1)
linked_list.insert_element(n2)
n3 = Node(8)
linked_list.insert_element(n3)
n4 = Node(3)
linked_list.insert_element(n4)
linked_list.print_list()