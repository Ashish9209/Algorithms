
This code defines a `DoublyLinkedList` and a `Node` class, which are used to implement a doubly linked list data structure. Here's a breakdown of the code and its functionality:

### `Node` Class

The `Node` class represents an individual element in the doubly linked list. Each node stores:
- A value (`value`)
- A reference to the next node (`next_node`)
- A reference to the previous node (`prev_node`)

**Methods:**
- `__init__`: Initializes a node with a value and optional references to the next and previous nodes.
- `set_next_node`: Sets the `next_node` reference for the node.
- `get_next_node`: Returns the `next_node` reference.
- `set_prev_node`: Sets the `prev_node` reference for the node.
- `get_prev_node`: Returns the `prev_node` reference.
- `get_value`: Returns the value stored in the node.

### `DoublyLinkedList` Class

The `DoublyLinkedList` class represents the doubly linked list itself. It manages a list where each node points to both its next and previous nodes.

**Attributes:**
- `head_node`: A reference to the first node in the list.
- `tail_node`: A reference to the last node in the list.

**Methods:**
- `__init__`: Initializes an empty doubly linked list with `head_node` and `tail_node` set to `None`.

- `add_to_head(new_value)`: 
  - Creates a new node with `new_value`.
  - If the list is not empty, updates the current head node to point back to the new node, and sets the new node’s `next_node` to the current head.
  - Updates `head_node` to the new node.
  - If the list was empty (i.e., `tail_node` is `None`), also sets `tail_node` to the new node.

- `add_to_tail(new_value)`:
  - Creates a new node with `new_value`.
  - If the list is not empty, updates the current tail node to point to the new node, and sets the new node’s `prev_node` to the current tail.
  - Updates `tail_node` to the new node.
  - If the list was empty (i.e., `head_node` is `None`), also sets `head_node` to the new node.

- `remove_head()`:
  - Removes the node at the head of the list.
  - Updates `head_node` to the next node in the list.
  - If the new head exists, updates its `prev_node` to `None`.
  - If the removed head was the only node (i.e., `head_node` equals `tail_node`), it calls `remove_tail()` to handle the single-node case.
  - Returns the value of the removed head node.

- `remove_tail()`:
  - Removes the node at the tail of the list.
  - Updates `tail_node` to the previous node in the list.
  - If the new tail exists, updates its `next_node` to `None`.
  - If the removed tail was the only node (i.e., `tail_node` equals `head_node`), it calls `remove_head()` to handle the single-node case.
  - Returns the value of the removed tail node.

- `remove_by_value(value_to_remove)`:
  - Searches for the first node with a value matching `value_to_remove`.
  - If found, removes that node by adjusting the `next_node` and `prev_node` references of its neighboring nodes.
  - If the node to be removed is the head or tail, it uses `remove_head()` or `remove_tail()`, respectively.
  - Returns the removed node.

- `stringify_list()`:
  - Constructs a string representation of the list by traversing from `head_node` to `tail_node`.
  - Appends the value of each node to the string, followed by a newline character.
  - Returns the concatenated string.

### Summary

- **`Node` class**: Represents each element of the doubly linked list with value and pointers to neighboring nodes.
- **`DoublyLinkedList` class**: Manages the list, providing methods to add, remove, and search for nodes, as well as to get a string representation of the list.