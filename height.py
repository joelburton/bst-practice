"""Find height of a binary tree."""

from bst import bst

def height(node):
    """Find height of tree.

        >>> height(bst)
        4
    """

    if node is None:
        return 0

    left_height = height(node.left)
    right_height = height(node.right)

    return max(left_height, right_height) + 1



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "w00t!"


    