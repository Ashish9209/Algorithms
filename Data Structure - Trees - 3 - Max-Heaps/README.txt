# Max-Heap Data Structure

## Characteristics of a Max-Heap

Think of the max-heap as a binary tree with the following qualities:

- **The root is the maximum value of the dataset.**
- **Every parent’s value is greater than its children.**

A max-heap tracks the maximum element as the element within a data set. It ensures that the largest element is always at the root of the tree.

## Maintaining the Heap Property

Max-heaps must maintain the heap property where parent values must be greater than their children.

### Adding Elements

When adding elements to a max-heap, the following process is used:

- **`heapify_up()`**: This method is used to maintain the heap property.
  - **Comparison**: Compare the new element with its parent.
  - **Swap if Necessary**: If the new element violates the heap property (i.e., if it is greater than its parent), swap the two values.

By using `heapify_up()`, the heap property is preserved, ensuring that every parent node remains greater than its child nodes.
