# Linked List Implementation in Python

This repository contains a simple implementation of a singly linked list in Python. It includes two classes: `Node` and `LinkedList`, which together provide the basic functionality of a linked list data structure.

## Classes

### `Node`

The `Node` class represents a single element in the linked list. Each node holds a value and a reference to the next node.

#### Methods

- **`__init__(self, value, next_node=None)`**
  - Initializes a new node with a specified value and an optional reference to the next node.
  
- **`get_value(self)`**
  - Returns the value stored in the node.
  
- **`get_next_node(self)`**
  - Returns the reference to the next node.
  
- **`set_next_node(self, next_node)`**
  - Sets the reference to the next node.

### `LinkedList`

The `LinkedList` class represents the linked list data structure. It manages nodes and provides operations to manipulate and traverse the list.

#### Methods

- **`__init__(self, value=None)`**
  - Initializes a new linked list with an optional head node value. If no value is provided, the head node is created with `None`.

- **`get_head_node(self)`**
  - Returns the head node of the list.
  
- **`insert_beginning(self, new_value)`**
  - Inserts a new node with the specified value at the beginning of the list.

- **`stringify_list(self)`**
  - Returns a string representation of the list, with each node's value on a new line.

- **`remove_node(self, value_to_remove)`**
  - Removes the first node in the list that matches the specified value.

## Example Usage

```python
# Create a new linked list with an initial value of 1
linked_list = LinkedList(1)

# Insert new values at the beginning of the list
linked_list.insert_beginning(2)
linked_list.insert_beginning(3)

# Print the linked list
print(linked_list.stringify_list())
# Output:
# 3
# 2
# 1

# Remove a node with value 2
linked_list.remove_node(2)

# Print the linked list again
print(linked_list.stringify_list())
# Output:
# 3
# 1
