
# Heap Implementation

This repository contains an implementation of a heap data structure. The heap is a type of binary tree that maintains a specific order property. This README file provides an overview of the functionality of key methods in the heap implementation.

## Methods

### `get_smaller_child_idx(self, idx)`

This method determines the index of the smaller child of a given node.

- **Parameters**:
  - `idx`: The index of the current node.

- **Returns**:
  - The index of the smaller child node. If only a left child exists, it returns the index of the left child. Otherwise, it compares the left and right children and returns the index of the smaller child.

### `heapify_up(self)`

This method restores the heap property by moving an element up the tree as long as it is smaller than its parent.

- **Process**:
  - Starts from the index of the newly added element (`self.count`).
  - Compares the element with its parent and swaps if the parent is greater.
  - Continues moving up the tree until the heap property is restored.
  
- **Prints**:
  - If the heap contains more than 10,000 elements, it prints a message showing the total number of elements and the number of swaps performed.

### `heapify_down(self)`

This method restores the heap property by moving an element down the tree to maintain the heap property.

- **Process**:
  - Starts from the root index (1), assuming the root has been swapped with another node.
  - Compares the element with its children and swaps with the smaller child if necessary.
  - Continues moving down the tree until the heap property is restored.

- **Prints**:
  - If the heap contains 10,000 or more elements, it prints a message showing the total number of elements and the number of swaps performed.

## Notes

- The methods assume that the heap list is 1-based indexed, meaning the first element is at index 1.
- The `heapify_up` and `heapify_down` methods are used to maintain the heap property after insertions and deletions.
- The heap operations are designed to handle large heaps efficiently.

## Usage

To use these methods, ensure that your heap class has a proper implementation of the following helper methods:

- `parent_idx(self, idx)`: Returns the index of the parent of the node at index `idx`.
- `left_child_idx(self, idx)`: Returns the index of the left child of the node at index `idx`.
- `right_child_idx(self, idx)`: Returns the index of the right child of the node at index `idx`.
- `child_present(self, idx)`: Checks if a child exists for the node at index `idx`.

Include these methods in your heap class to provide full heap functionality.


