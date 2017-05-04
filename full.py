"""Is a BST full?

A "full" BST is one where the tree is fully filled, like this:

    2            4                4
   1 3        2     6          2     6
             1 3   5 7        1 3

In a full tree, every node has either zero or two children.

Our example BST is not fully filled --- there is an empty spot in
the right child of the 1.

            5
        3       7
      1   4   6   9
     0
"""

from bst import bst, BNode as N


def is_full(node):
    """Is this fully filled?

        >>> is_full(N(2, N(1), N(3)))
        True

        >>> is_full(N(4, N(2, N(1), N(3)), N(6, N(5), N(7))))
        True

        >>> is_full(N(4, N(2, N(1), N(3)), N(6)))
        True

        >>> is_full(bst)
        False
    """

    if not node:
        return True

    if (node.left is None) != (node.right is None):
        return False

    if is_full(node.left) and is_full(node.right):
        return True

    return False


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "w00t!"
