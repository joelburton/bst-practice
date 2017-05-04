"""Is a BST balanced?

Two similar-but-different approaches.
"""

import math
from bst import bst, BNode

def is_balanced_v1(node):
    """Is this tree balanced?

    Another way to think about the problem: for every node, if the
    height of its left subtree and the height of its right subtree
    are different by more than 1, it cannot be balanced.

    This is the naive approach shown at
    http://algorithms.tutorialhorizon.com/find-whether-if-a-given-binary-tree-is-balanced/

    The runtime of this isn't great, since it keeps recalculating the
    height of the going down --- so v3 for a much better idea.

        >>> is_balanced_v1(bst)
        True

        >>> bad = BNode(3, BNode(2, BNode(1)))
        >>> is_balanced_v1(bad)
        False
    """

    if not node:
        return True

    lh = get_height(node.left)
    rh = get_height(node.right)

    if abs(lh - rh) > 1:
        return False

    return is_balanced_v1(node.left) and is_balanced_v1(node.right)


def get_height(node):
    """Get height of tree.

        >>> get_height(bst)
        4
    """

    if not node:
        return 0

    return max(get_height(node.left), get_height(node.right)) + 1


#####################################################################


class ImbalancedSubtree(Exception):
    """Exception when we find an imbalanced subtree."""


def is_balanced_v2(node):
    """Is this tree balanced?

    Another way to think about the problem: for every node, if the
    height of its left subtree and the height of its right subtree
    are different by more than 1, it cannot be balanced.

    This is the better approach shown at
    http://algorithms.tutorialhorizon.com/find-whether-if-a-given-binary-tree-is-balanced/
    except that at the point we find any node that is imbalanced, we
    raise an exception that we catch in the outer function. This
    simplifies things a bit.

        >>> is_balanced_v2(bst)
        True

        >>> bad = BNode(3, BNode(2, BNode(1)))
        >>> is_balanced_v2(bad)
        False
    """

    try:
        is_node_balanced(node)
        return True
    except ImbalancedSubtree:
        return False


def is_node_balanced(node):
    """Is this subtree balanced? If so, return it's height.

    This is just like get_height, above, except that, while finding
    the height, if it detects that it is imbalanced, it raises an
    exception.

        >>> is_node_balanced(BNode(2, BNode(1), BNode(3)))
        2

        >>> is_node_balanced(BNode(3, BNode(2, BNode(1))))
        Traceback (most recent call last):
            ...
        ImbalancedSubtree
    """

    if not node:
        return 0

    lh = is_node_balanced(node.left)
    rh = is_node_balanced(node.right)

    if abs(lh - rh) > 1:
        raise ImbalancedSubtree

    return max(lh, rh) + 1


#####################################################################


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "w00t!"
