
# Binary Search Tree (BST) Implementation

This Python code defines a basic implementation of a Binary Search Tree (BST) with the following functionalities:

- **Insertion of nodes**
- **Searching for nodes by value**
- **Depth-first traversal**

## Code Explanation

### 1. Import Statement

```python
import random
```
- Imports the `random` module, which is used to generate random integers for testing the BST.

### 2. BinarySearchTree Class

The `BinarySearchTree` class represents a node in the binary search tree and contains methods for various operations.

#### Initialization

```python
class BinarySearchTree:
  def __init__(self, value, depth=1):
    self.value = value
    self.depth = depth
    self.left = None
    self.right = None
```
- **`__init__` Method**: Initializes a new node with a given `value` and `depth`. 
  - **`value`**: The value stored in the node.
  - **`depth`**: The depth of the node in the tree (root node starts at depth 1).
  - **`left`**: Points to the left child node.
  - **`right`**: Points to the right child node.

#### Insertion

```python
  def insert(self, value):
    if (value < self.value):
      if (self.left is None):
        self.left = BinarySearchTree(value, self.depth + 1)
        print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
      else:
        self.left.insert(value)
    else:
      if (self.right is None):
        self.right = BinarySearchTree(value, self.depth + 1)
        print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
      else:
        self.right.insert(value)
```
- **`insert` Method**: Inserts a new node with the specified `value` into the BST.
  - **Left Subtree**: If `value` is less than the current node's `value`, it is added to the left subtree.
  - **Right Subtree**: If `value` is greater than or equal to the current node's `value`, it is added to the right subtree.
  - **Recursive Insertion**: If the appropriate child node already exists, the `insert` method is called recursively.

#### Searching for a Node by Value

```python
  def get_node_by_value(self, value):
    if (self.value == value):
      return self
    elif ((self.left is not None) and (value < self.value)):
      return self.left.get_node_by_value(value)
    elif ((self.right is not None) and (value >= self.value)):
      return self.right.get_node_by_value(value)
    else:
      return None
```
- **`get_node_by_value` Method**: Searches for a node with the specified `value`.
  - **Current Node**: Returns the node if its `value` matches.
  - **Left Subtree**: Searches in the left subtree if the `value` is less than the current node's `value`.
  - **Right Subtree**: Searches in the right subtree if the `value` is greater than or equal to the current node's `value`.
  - **Return `None`**: If the value is not found.

#### Depth-First Traversal

```python
  def depth_first_traversal(self):
    if (self.left is not None):
      self.left.depth_first_traversal()
    print(f'Depth={self.depth}, Value={self.value}')
    if (self.right is not None):
      self.right.depth_first_traversal()
```
- **`depth_first_traversal` Method**: Performs an inorder depth-first traversal of the BST.
  - **Left Subtree**: Recursively visits the left subtree.
  - **Current Node**: Prints the depth and value of the current node.
  - **Right Subtree**: Recursively visits the right subtree.

### Example Usage

```python
print("Creating Binary Search Tree rooted at value 15:")
tree = BinarySearchTree(15)

for x in range(10):
  tree.insert(random.randint(0, 100))
  
print("Printing the inorder depth-first traversal:")
tree.depth_first_traversal()
```
- **Create Tree**: Initializes a BST with the root value `15`.
- **Insert Random Values**: Inserts 10 random integers between 0 and 100 into the BST.
- **Print Traversal**: Prints the inorder traversal of the BST, showing the depth and value of each node.

## Summary

The provided code demonstrates a basic implementation of a Binary Search Tree in Python, including methods for inserting nodes, searching for nodes by value, and performing depth-first traversal. The BST maintains a sorted order of elements, allowing efficient search and insertion operations.
```
