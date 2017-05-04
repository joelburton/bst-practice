"""Does binary search tree contain node?"""

from bst import bst

def contains(node, val):
    """Does tree starting at node contain node with val?

        >>> contains(bst, 5)
        True

        >>> contains(bst, 1)
        True

        >>> contains(bst, 2)
        False

        >>> contains(bst, 6)
        True
    """

    while node is not None:
        if node.data == val:
            return True

        if val < node.data:
            node = node.left

        else:
            node = node.right

    return False


def rcontains(node, val):
    """Does tree starting at node contain node with val?
 
        >>> rcontains(bst, 5)
        True

        >>> rcontains(bst, 1)
        True

        >>> rcontains(bst, 2)
        False

        >>> rcontains(bst, 6)
        True
    """

    if node is None:
        return False

    if node.data == val:
        return True

    if val < node.data:
        return rcontains(node.left, val)

    else:
        return rcontains(node.right, val)


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "w00t!"