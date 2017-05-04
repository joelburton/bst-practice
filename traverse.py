"""Traverse binary trees."""

from bst import bst

def preorder(node):
    """Pre-order traversal of tree.

    This works out to be "top-down, left-to-right"

        >>> preorder(bst)
        5 3 1 0 4 7 6 9
    """

    if node is None:
        return

    print node.data,
    preorder(node.left)
    preorder(node.right)


def postorder(node):
    """Post-order traversal of tree.

    This works out to be "bottom-up, left-to-right"

        >>> postorder(bst)
        0 1 4 3 6 9 7 5
    """

    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print node.data,


def inorder(node):
    """In-order traversal of tree.

        >>> inorder(bst)
        0 1 3 4 5 6 7 9
    """

    if node is None:
        return

    inorder(node.left)
    print node.data,
    inorder(node.right)


def rev_inorder(node):
    """Reverse in-order traversal of tree.

        >>> rev_inorder(bst)
        9 7 6 5 4 3 1 0
    """

    if node is None:
        return

    rev_inorder(node.right)
    print node.data,
    rev_inorder(node.left)



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "w00t!"