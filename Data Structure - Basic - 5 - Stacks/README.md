This code implements a `Stack` data structure using a linked list, with operations to add (push) and remove (pop) items from the top of the stack. It uses a `Node` class, which is imported from an external module. Here’s a detailed breakdown:

### `Stack` Class

The `Stack` class represents a stack data structure, which follows the Last In, First Out (LIFO) principle. This means that the last item added to the stack is the first one to be removed.

**Attributes:**
- `top_item`: A reference to the top node of the stack.
- `size`: The current number of items in the stack.
- `limit`: The maximum number of items that the stack can hold.

**Methods:**

1. **`__init__(self, limit=1000)`**:
   - Initializes a new stack.
   - Sets `top_item` to `None` (indicating an empty stack), `size` to `0`, and `limit` to the specified maximum capacity (default is 1000).

2. **`push(self, value)`**:
   - Adds a new item (`value`) to the top of the stack.
   - Checks if there is space in the stack using `has_space()`.
   - Creates a new `Node` with the given `value`.
   - Sets the `next_node` of the new node to the current `top_item`.
   - Updates `top_item` to the new node.
   - Increases the `size` of the stack by `1`.
   - Prints a message indicating the addition of the item.
   - If the stack is full, prints a message indicating there’s no room.

3. **`pop(self)`**:
   - Removes and returns the item from the top of the stack.
   - Checks if the stack is not empty using `is_empty()`.
   - Retrieves the `top_item`, updates `top_item` to the next node in the stack.
   - Decreases the `size` by `1`.
   - Prints a message indicating the item being removed.
   - Returns the value of the removed node.
   - If the stack is empty, prints a message indicating that there are no items to remove.

4. **`peek(self)`**:
   - Returns the value of the item at the top of the stack without removing it.
   - Checks if the stack is not empty using `is_empty()`.
   - Prints a message if the stack is empty.

5. **`has_space(self)`**:
   - Returns `True` if there is space to add more items to the stack (i.e., the current `size` is less than `limit`).
   - Returns `False` otherwise.

6. **`is_empty(self)`**:
   - Returns `True` if the stack is empty (`size == 0`).
   - Returns `False` otherwise.

### Example Usage

The example code demonstrates creating a stack and performing various operations:

1. **Creating a Stack**:
   - `pizza_stack = Stack(6)` creates a stack with a maximum capacity of 6.

2. **Pushing Items**:
   - `push` method adds pizzas to the stack until it reaches its capacity.
   - If attempting to add more items than the `limit`, the code prints "No room for pizza #7!".
   - The commented line allows you to test pushing beyond the stack's capacity.

3. **Peeking**:
   - `peek()` shows the top pizza in the stack without removing it.

4. **Popping Items**:
   - `pop` method removes pizzas from the top of the stack.
   - After popping all items, attempting to pop from an empty stack prints "All out of pizza."

5. **Uncommented Code**:
   - The commented lines indicate where you can test pushing and popping beyond the stack’s limit.

### Summary

This `Stack` class manages a collection of items using a linked list. It provides methods to:
- **Add items** (`push`), respecting a maximum capacity.
- **Remove items** (`pop`) from the top of the stack.
- **Inspect the top item** (`peek`) without removing it.
- **Check for space** and whether the stack is empty.

The code also includes example usage that simulates managing a stack of pizzas, demonstrating stack operations and handling scenarios when the stack is full or empty.