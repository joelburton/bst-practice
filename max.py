"""What's the largest value in a BST?

It would be naive to search the entire tree for a value ---
instead, we can always find the largest value as the rightmost
value.
"""

from bst import bst

def get_max(node):
    """Get largest value.

        >>> get_max(bst)
        9
    """

    if node is None:
        return None

    while node.right is not None:
        node = node.right

    return node.data


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "w00t!"
