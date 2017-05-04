"""Sample binary search tree.

            5
        3       7
      1   4   6   9
     0
"""

class BNode(object):
    """Binary tree node."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# The tree we'll use for many examples in this directory:

bst = BNode(5,
            BNode(3,
                  BNode(1,
                        BNode(0)),
                  BNode(4)),
            BNode(7,
                  BNode(6),
                  BNode(9)))
