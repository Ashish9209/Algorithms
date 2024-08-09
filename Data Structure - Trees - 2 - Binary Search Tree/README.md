
# Binary Search Tree (BST) Overview

A Binary Search Tree (BST) is a type of binary tree where each node has at most two children, referred to as the left and right children. It maintains a sorted order of elements, which allows efficient searching, insertion, and deletion operations.

## Node Properties

Each node in a BST is an instance of the `BinarySearchTree` class and has the following properties:

- **Value**: Represents the data stored in the node.
- **Depth**: Indicates the level of the node in the tree. The root node has a depth of 1, while nodes at lower levels have a greater depth.
- **Left Child**: An instance variable pointing to the left child node, which is a BST itself and contains data less than the parent node's data.
- **Right Child**: An instance variable pointing to the right child node, which is a BST itself and contains data greater than or equal to the parent node's data.

## Depth-First Traversal

Depth-first traversal explores as far down a branch as possible before backtracking. There are three common types of depth-first traversal:

1. **Preorder Traversal**:
   - **Order**: Visit the current node first, then traverse the left subtree, followed by the right subtree.
   - **Usage**: Useful for creating a copy of the tree or for prefix expression evaluation.

2. **Inorder Traversal**:
   - **Order**: Traverse the left subtree first, visit the current node, then traverse the right subtree.
   - **Usage**: Useful for retrieving the elements of a BST in sorted order.

3. **Postorder Traversal**:
   - **Order**: Traverse the left subtree first, then the right subtree, and finally visit the current node.
   - **Usage**: Useful for deleting nodes or performing postfix expression evaluation.

## `BinarySearchTree` Class

The `BinarySearchTree` class contains several key methods:

### 1. `.insert(value)`

- **Purpose**: Inserts a node with the specified value at the correct location in the BST.
- **Time Efficiency**:
  - **Balanced Tree**: O(log N), where N is the number of nodes. The maximum depth of a balanced tree is log(N), so this method makes at most log(N) comparisons.
  - **Imbalanced Tree**: O(N), where all nodes are on one side of the tree, leading to a worst-case performance of N comparisons.

### 2. `.get_node_by_value(value)`

- **Purpose**: Retrieves a node in the tree by its value.
- **Time Efficiency**:
  - **Balanced Tree**: O(log N), similar to insertion, making at most log(N) comparisons.
  - **Imbalanced Tree**: O(N), in the worst case where the tree is skewed.

### 3. `.depth_first_traversal()`

- **Purpose**: Prints the inorder traversal of the BST.
- **Time Efficiency**: O(N), as it visits every node in the tree.

## Additional Features (Future Enhancements)

To further enhance the `BinarySearchTree` implementation, consider adding:

- **`.delete()` Method**: Allows removal of a node from the BST while maintaining the tree's properties.
- **Self-Balancing Feature**: Maintains the balance of the tree during insertions and deletions, ensuring that the tree remains balanced with a maximum depth of log(N). This guarantees O(log N) time complexity for insertion and search operations.

## Summary

The Binary Search Tree is a dynamic and efficient data structure for managing sorted data. It provides efficient insertion and search operations while maintaining a sorted order. Advanced features like self-balancing and deletion methods can further enhance its functionality and performance.

