# Deque Data Structure

A **deque** (double-ended queue) is a versatile data structure that allows for insertions and deletions at both ends. It combines the functionalities of both a queue and a stack.

## Key Operations

1. **Insertions:**
   - `insertFront(item)`: Inserts an element at the front of the deque.
   - `insertLast(item)`: Inserts an element at the rear of the deque.

2. **Deletions:**
   - `removeFront()`: Removes and returns the element at the front of the deque.
   - `removeLast()`: Removes and returns the element at the rear of the deque.

3. **Utility Methods:**
   - `isEmpty()`: Checks if the deque is empty and returns `True` if it is, otherwise `False`.
   - `size()`: Returns the number of elements in the deque.

## Implementation

A deque can be implemented using:

- **Doubly-Linked List**: Allows for efficient insertions and deletions at both ends. Operations are generally O(1) in time complexity.
- **Array**: Can also be used for implementation, with operations achieving O(1) time complexity.

## Benefits

- **Flexibility**: Deques support both “First in First Out” (FIFO) and “Last in First Out” (LIFO) functionalities.
- **Efficiency**: Operations such as insertion and deletion at both ends are efficient and occur in constant time, O(1), when implemented correctly.

A deque provides the flexibility to switch between different usage patterns without restrictions on where elements can be inserted or removed.
