"""How many nodes in a binary tree?"""

from bst import bst


def count(node):
    """How many nodes in a BST?

        >>> count(bst)
        8
    """

    if not node:
        return 0

    return count(node.left) + count(node.right) + 1


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "w00t!"
