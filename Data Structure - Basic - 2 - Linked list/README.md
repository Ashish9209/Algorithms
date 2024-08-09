# Linked List Implementation in Python

This document provides an overview of a simple linked list implementation in Python. The implementation consists of two classes: `Node` and `LinkedList`.

## Node Class

The `Node` class represents a single node in the linked list. Each node contains a value and a reference to the next node.

### Methods

- **`__init__(self, value, next_node=None)`**
  - Initializes a new node with a specified value and an optional reference to the next node.
  
- **`get_value(self)`**
  - Returns the value of the node.
  
- **`get_next_node(self)`**
  - Returns the reference to the next node.
  
- **`set_next_node(self, next_node)`**
  - Sets the reference to the next node.

### Example

```python
node1 = Node(1)
node2 = Node(2, node1)
print(node2.get_value())  # Output: 2
print(node2.get_next_node().get_value())  # Output: 1
