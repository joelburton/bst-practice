"""Is a BST valid?

A valid BST follows a left-is-less, right-is-greater rule.
"""

from bst import bst, BNode as N

def is_valid(node):
    """Is this node valid?

        >>> is_valid(bst)
        True

        >>> is_valid(N(2, N(1)))
        True

        >>> is_valid(N(1, N(2)))
        False

        >>> is_valid(N(4, N(2, N(1), N(3)), N(6, N(5), N(7))))
        True

        >>> is_valid(N(4, N(2, N(99), N(3)), N(6, N(5), N(7))))
        False
    """

    return ok(node, None, None)


def ok(node, minv, maxv):
    """Does this node fall within legal values?"""

    if node is None:
        return True

    d = node.data

    # Check if within range, but in a way where either minv or
    # maxv might not yet be separately

    if minv is not None and d <= minv:
        return False

    if maxv is not None and d >= maxv:
        return False

    # Recurse into children, narrowing range
    return (ok(node.left, minv, d) and ok(node.right, d, maxv))


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "w00t!"
