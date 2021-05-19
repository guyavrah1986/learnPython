

class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


def is_root_to_leaf_path_sum_exists(node: object, sum_to_check: int) -> bool:
    func_name = "is_root_to_leaf_path_sum_exists - "
    if node is None:
        return sum_to_check == 0

    exists = False
    sub_sum = sum_to_check - node.val
    if sub_sum == 0 and node.left is None and node.right is None:
        return True

    if node.left is not None:
        exists = exists or is_root_to_leaf_path_sum_exists(node.left, sub_sum)
    if node.right is not None:
        exists = exists or is_root_to_leaf_path_sum_exists(node.right, sub_sum)

    return exists


def find_if_there_is_root_to_leaf_sum_path(sum_to_check: int) -> bool:
    func_name = "findIfThereIsRootToLeafSumPath - "
    print(func_name + "about to check if there is root to leaf path that sums up to:" + str(sum_to_check))
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)

    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)
    exists = is_root_to_leaf_path_sum_exists(root, sum_to_check)
    if exists:
        print(func_name + "there is a root to leaf path that sums to:" + str(sum_to_check) + " in the given tree")
    else:
        print(func_name + "there is NO path in the given tree")


sum_to_check = 21
find_if_there_is_root_to_leaf_sum_path(sum_to_check)



