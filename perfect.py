"""Is this tree "perfect?", two different ways.

A perfect binary tree is one where every node has zero or two children,
and all leaves are at the same rank. These trees are absolutely perfect
triangles, like these:

    2            4
   1 3        2     6
             1 3   5 7
"""

import math
from bst import bst, BNode
from count import count
from height import height

def is_perfect(node):
    """Is this tree perfect?

    Math observation: a perfect tree always has a number of nodes
    that is equal to the 2 ** height - 1.

        >>> is_perfect(BNode(1))
        True

        >>> is_perfect(BNode(2, BNode(1), BNode(3)))
        True

        >>> is_perfect(bst)
        False
    """

    return count(node) == 2 ** height(node) - 1


#######################################################################


def is_perfect_v2(node):
    """Is this tree perfect?

    Math observation: a perfect tree always has a number of nodes
    that is equal to the 2 ** height - 1. We don't need to get the
    height separately, though -- we can check if the # nodes is valid
    for any height:

        >>> is_perfect_v2(BNode(1))
        True

        >>> is_perfect_v2(BNode(2, BNode(1), BNode(3)))
        True

        >>> is_perfect_v2(bst)
        False
    """

    nnodes = count(node)

    return math.log(nnodes + 1, 2) == int(math.log(nnodes + 1, 2))



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "w00t!"
