# MaxHeap Class Implementation

The `MaxHeap` class represents a max heap data structure. In a max heap, the key at a parent node is always greater than or equal to the keys of its children, and the highest key is at the root. This class provides methods to add elements to the heap and ensure that the heap property is maintained.

## Code Explanation

### Initialization

```python
class MaxHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0
```
- **`__init__` Method**: Initializes an empty heap.
  - **`heap_list`**: A list to store the elements of the heap. The first element is `None` to facilitate 1-based indexing for simplicity.
  - **`count`**: Keeps track of the number of elements in the heap.

### Heap Helper Methods

These methods assist in navigating the heap and are used internally to maintain the heap structure.

```python
  def parent_idx(self, idx):
    return idx // 2

  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1
```

- **`parent_idx(self, idx)`**: Returns the index of the parent node of the node at index `idx`.
- **`left_child_idx(self, idx)`**: Returns the index of the left child node of the node at index `idx`.
- **`right_child_idx(self, idx)`**: Returns the index of the right child node of the node at index `idx`.

These methods help in navigating the heap structure based on indices.

### Adding Elements

```python
  def add(self, element):
    self.count += 1
    print("Adding: {0} to {1}".format(element, self.heap_list))
    self.heap_list.append(element)
    self.heapify_up()
```

- **`add(self, element)`**: Adds a new element to the heap.
  - **`self.count += 1`**: Increments the count of elements in the heap.
  - **`self.heap_list.append(element)`**: Appends the new element to the end of the heap list.
  - **`self.heapify_up()`**: Ensures the heap property is maintained after adding the new element.

### Heapify Up

```python
  def heapify_up(self):
    print("Heapifying up")
    idx = self.count
    while self.parent_idx(idx) > 0:
      child = self.heap_list[idx]
      parent = self.heap_list[self.parent_idx(idx)]
      if parent < child:
        print("swapping {0} with {1}".format(parent, child))
        self.heap_list[idx] = parent
        self.heap_list[self.parent_idx(idx)] = child
      idx = self.parent_idx(idx)
    print("Heap Restored {0}".format(self.heap_list))
```

- **`heapify_up(self)`**: Restores the heap property by moving the newly added element up the heap if it is greater than its parent.
  - **`idx = self.count`**: Starts at the index of the newly added element.
  - **`while self.parent_idx(idx) > 0`**: Continues as long as the current index has a valid parent.
  - **`child = self.heap_list[idx]`**: The value of the current node.
  - **`parent = self.heap_list[self.parent_idx(idx)]`**: The value of the parent node.
  - **`if parent < child`**: Checks if the current node is greater than its parent.
    - **Swapping**: If so, swaps the parent and child values to maintain the heap property.
  - **`idx = self.parent_idx(idx)`**: Moves to the parent node and continues heapifying up.

### Summary

The `MaxHeap` class provides basic functionality for a max heap:
- **Initialization**: Sets up an empty heap.
- **Helper Methods**: Navigates the heap based on indices.
- **Adding Elements**: Appends a new element and maintains the heap property.
- **Heapify Up**: Ensures the max heap property is maintained by moving elements up the tree as necessary.

This implementation maintains the max heap property, where each parent node is greater than or equal to its children, ensuring that the maximum value is always at the root.
```