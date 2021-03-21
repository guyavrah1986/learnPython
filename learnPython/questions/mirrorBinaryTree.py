# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode) -> TreeNode:
    if root is None:
        return root

    invert_tree(root.left)
    invert_tree(root.right)
    tmp = root.right
    root.right = root.left
    root.left = tmp
    return root


""" Helper function to print Inorder traversal."""
def inOrder(node):
    if (node == None):
        return

    inOrder(node.left)
    print(node.val, end=" ")
    inOrder(node.right)


# Driver code
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    """ Print inorder traversal of 
        the input tree """
    print("Inorder traversal of the",
          "constructed tree is")
    inOrder(root)

    """ Convert tree to its mirror """
    invert_tree(root)

    """ Print inorder traversal of  
        the mirror tree """
    print("\nInorder traversal of",
          "the mirror trees ")
    inOrder(root)
