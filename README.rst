Binary Search Trees
===================

:author: Joel Burton <joel@joelburton.com>


Definitions
-----------

Tree
    A structure made up of nodes, where a node has
    0 or 1 parent (the node with no parents is a "root").
    Each node can have 0 or more children. Nodes without
    children are called "leaf nodes". There may or may
    not be a special reason for the arrangement of the
    nodes. Trees that aren't limited to a certain number
    of children-per-node are sometimes called "general
    trees" or "n-ary trees" (instead of "*bi*-nary, they're
    *some-value-of-n*-ary).

Binary Tree
    A tree where each node has 0, 1, or 2 children.
    Typically labeled "left" and "right". Note that
    for a binary trees, there's no specific rule about
    how the parents/children are ordered.

Binary Search Tree
    A common specialization of a binary tree where there
    is a rule about parents and children. Typically, this
    rule is "all values less than mine are left of me, and
    all values greater than mine are right of me".

Runtimes of BSTs
----------------

Be careful about just saying the "runtime of a binary search tree
is ``O(log n)``"! Always ask "the runtime of
*what action*?""

- For example, finding the immediate children of the
  root is ``O(1)`` --- since we're only looking 1 level down, it
  doesn't matter how deep the tree is

- Another example: printing all of the nodes in the tree is
  ``O(n)`` --- you have to look at each node to print it!

**Searching**: For searching a BST, the you can talk about this
in two possible ways: in terms of the height of the tree, or
in terms of the number of nodes.

Consider this BST::

            5
        3       7
      1   4   6   9
     0

The runtime to search this BST for a value is ``O(h)``, where `h`
is the height of the tree. This is true for *all* binary trees:
the runtime to search it always *linear to the height*.

We could also express the runtime in terms of the number of
nodes. For that same tree, given that it's balanced, the
runtime to search it is ``O(log n)``, where `n` is the number of nodes.

However, we could have another *valid* BST with those same values,
like this::

  0
    1
      3
        4
          5
            6
              7
                9

The runtime to search this is still ``O(h)`` *[linear to the height]*.
It's not ``O(log n)``, though, since this tree isn't balanced --- it's
``O(n)`` to search.

A perfectly-balanced BST will have a height that can be found with::

    import math
    math.ceil(math.log(n - 1, 2))

(that is, the smallest integer that is equal to or greater than
the logarithm-2 of the number of nodes minus 1).

So, for example, to store 6 nodes, you could do this in a tree
that is 3 high. (You could store up to 7 nodes in a 3-height BST;
to store more, you'd need another rank).

(However, just because a BST uses the fewest number of ranks
doesn't always mean its balanced --- to be balanced, there's a stricter
requirement: for every node, the height of its left-subtree can
vary from the height of its right-subtree by, at most, 1).


Self-Balancing BSTs
-------------------

There are some intermediate-difficult algorithms to keep a BST
balanced, even as new items are added/deleted. Two popular tree
styles for this are:

- AVL Trees (named after the inventors)

- Red/Black Tree (named because you mark nodes as "red" or "black"
  given properties about them)

The algorithms to make these are in most algorithm textbooks.
It's not the kind of thing most developers have memorized (I don't!).
However, you can learn a few things about them:

- both of these self-balancing BSTs require that you keep
  track of some special information about each node (the
  "balance factor" for AVL, the "red/black" for red/black).

- both can add and delete new elements in ``O(log n)`` runtime,
  assuming tree is already balanced.

- both don't guarantee that the tree is *perfectly balanced*
  (if you made a BST from scratch, you can often be more
  efficient than an AVL or R/B). However, the amount that they
  are inefficient is a constant multiplier of the perfect
  height (for AVL, they're, at most, ~1.4444 x perfect height).
  Since that maximum difference is a constant, and not related
  to `n`, we can get rid of it in runtime analysis, and still
  say that searching/adding/deleting is ``O(log n)``.


What Are BSTs Good For?
-----------------------

We want to keep track of data about employees: their name
and SSN, so we can look people up by SSN::

    Jane        111-22-1234
    Jessica     222-22-1234
    Jada        333-22-1234
    Juanita     444-22-1234
    ...

We could keep this in a dictionary, like this::

    {"111-22-1234": "Jane", "222-22-1234": "Jessica"}

If we did this, then we could easily find a single person by SSN::

    emps["111-22-1234"]     # Jane!

We could find that someone was missing easily, too::

    emps["999-11-9999"]     # KeyError, so no matching emp!

Both of these are easy ``O(1)`` operations in a dictionary.

However, there are things dictionaries aren't good for:

- finding employee with smallest (or largest) SSN

- finding employees with SSNs less-than or greater-than a value
  ("find everyone with an SSN less than 222" or "starting with 4")

- finding employees by SSN ranges ("find everyone whose SSN is
  between 300-\* and 800-\*")

With a dictionary, all of these would be ``O(n)`` operations, since
we'd have to look at every single item.

For a BST, simple lookup to match an SSN is ``O(log n)`` --- worse than
a dictionary. However, we could find things like the smallest or
largest SSN is ``O(log n)`` --- a big improvement over ``O(n)``!


Duplicate Nodes
---------------

Most BSTs are defined to have no duplicate nodes.

If you do allow duplicate nodes in a BST, you need to decide
whether equal nodes go the left or right (it needs to be one, since
you always need to unambiguously know which direction to head!)

Note that a BST that allows duplicate nodes cannot be guaranteed
to be balanceable. For example, here's a BST that puts dupes on
the right::

  0
    0
      0
        0
          0
            0
              0

That BST has 7 nodes, so, in theory, it could be made in only
3 balanced ranks (log2(7 + 1) = 3). However, since dupes must
go on one side, there's no way to make this (pathologically evil)
BST any more balanced than it is.

Iteration Versus Recursion
--------------------------

**Fact:** any algorithm that you can solve with a loop can be solved
with recursion.

**Fact:** any algorithm that you can solve with recursion can be
solved iteratively.

**Strongly Held Opinion:** some problems just seem more sensible
with one style or another.

When you have an algorithm that needs to make a single choice at
each step, it's often easier to write it as a loop. For example,
*searching* a BST feels linear: at each point, you know whether
you have to go left or right; you don't need to keep track of the
"path not chosen". This is usually easier to visualize as a loop::

    while not fallen off bottom of tree:
        are you the node i want? if so, win!
        if less, head left
        if more, head right

When you have an algorithm that needs to explore more than one
path (like *printing* every node in a BST), it's often easier to
think about this recursively. You *could* do it in a loop, by
keeping a "to_visit" queue/stack of all the nodes you need to
visit, and peel off one each time, adding more nodes-to-do as you
go (see examples in our "Trees" lecture for looking for Hermoine).

However, these kinds of problems are often easier to think about
recursively::

    while on a node:
        print data
        do-same-on-the-left-recursively
        do-same-on-the-right-recursively

This kind of recursion is often called "multiple recursion" ---
inside the recursive function, you're firing off more than one
call to the function in question.


Code Challenges
---------------

Easier
++++++

These problems are linear --- they don't require a recursive version.

bst.py
  Make a class for a binary tree.

contains.py
  Does a BST contain a node with given value?

max.py
  What is the largest value in a BST?

rank.py
  For a BST, what is the rank (level) of the node with the given value?

Medium
++++++

These problems are a bit harder --- they require walking the tree,
either recursively or using a stack to keep track of the traversal:

count.py
  How many nodes are in a binary tree?

height.py
  What is the height of a binary tree?

full.py
  Is a given tree "full" (every node has either zero or two children)

traverse.py
  Traverse a BST, printing every node in ascending order

Harder
++++++

These problems are a bit harder still --- they require a recursive
or stack-maintaining version, plus they require some thought about
how to solve the problem at hand, separate from the traversal.

create.py
  Create a balanced binary tree, given a list of input

perfect.py
  Is a given tree "perfect" (perfect triangle; full and also every
  leaf is at same level)

valid.py
  Is a BST valid (does it follow the left-less, right-greater rule?)

balanced.py
  Is a BST balanced?


Misc Stuff
----------

An excellent followup to this is the chapter on Trees at
http://interactivepython.org/runestone/static/pythonds/Trees/toctree.html

- BSTs aren't the only kind of binary trees. They are the most common,
  but there are other kinds. In particular, there's another kind of
  binary tree, a "binary heap", which is very efficient (``O(1)``) for
  finding the smallest/largest item in a collection, and can add/delete items
  in ``O(log n)`` time. These have a special arrangement of the
  nodes in the tree, like a BST, but it's not the "less-on-left,
  greater-on-right" that a BST uses.

- You may hear someone refer to a "BTree". This isn't just a binary
  tree; it's a very specific kind of BST that can be self-balancing
  and doesn't need to be read into memory all at once (you can work
  on them directly off a disk). These are often used for database
  indexes.
