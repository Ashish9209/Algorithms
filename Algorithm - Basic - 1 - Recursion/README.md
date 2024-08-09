# Understanding Recursive Data Structures

Data structures can also be recursive. One such data structure is the tree.

## Trees

Trees are a recursive data structure because their definition is self-referential. A tree is a data structure that contains a piece of data and references to other trees!

### Parent and Child Trees

- Trees that are referenced by other trees are known as **children**.
- Trees that hold references to other trees are known as **parents**.

A tree can be both a parent and a child.

## Binary Search Trees

We’ll focus on building a special type of tree called a **binary search tree**. 

### Properties of Binary Search Trees

- A binary search tree references at most two children per tree node.
- The **left** child of the tree must contain a value lesser than its parent.
- The **right** child of the tree must contain a value greater than its parent.

## Implementation Notes

Trees are an abstract data type, meaning we can implement our version in a number of ways as long as we follow the rules mentioned above.
