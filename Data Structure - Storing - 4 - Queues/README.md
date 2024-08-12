
This code implements a `Queue` class that uses a linked list structure for storing elements, leveraging a `Node` class from an external module. Here’s a detailed breakdown of how it works:

### `Queue` Class

The `Queue` class provides a basic implementation of a queue data structure. A queue is a collection of elements that follows the First In, First Out (FIFO) principle. Elements are added to the end (tail) and removed from the front (head).

**Attributes:**
- `head`: Points to the first node in the queue.
- `tail`: Points to the last node in the queue.
- `max_size`: Optional maximum capacity of the queue. If `None`, the queue has unlimited capacity.
- `size`: Current number of elements in the queue.

**Methods:**

1. **`__init__(self, max_size=None)`**:
   - Initializes a new queue.
   - Sets `head` and `tail` to `None`, `max_size` to the provided value or `None`, and `size` to `0`.

2. **`enqueue(self, value)`**:
   - Adds a new element (`value`) to the end of the queue.
   - Checks if there is space in the queue using `has_space()`.
   - Creates a new `Node` with the given `value`.
   - If the queue is empty (i.e., `head` is `None`), sets both `head` and `tail` to the new node.
   - Otherwise, links the new node to the end of the queue by setting the `next_node` of the current `tail` to the new node and then updates `tail` to the new node.
   - Increases the `size` of the queue by `1`.
   - Prints a message indicating the addition of the new element.

3. **`dequeue(self)`**:
   - Removes and returns the element from the front of the queue.
   - Checks if the queue is not empty (`size > 0`).
   - Retrieves the `head` node and prints a message indicating the served element.
   - If there is only one element in the queue, sets both `head` and `tail` to `None`.
   - Otherwise, updates `head` to point to the next node in the queue.
   - Decreases the `size` of the queue by `1`.
   - Returns the value of the removed node.
   - Prints a message if the queue is empty.

4. **`peek(self)`**:
   - Returns the value of the element at the front of the queue without removing it.
   - Checks if the queue is not empty (`size > 0`).
   - Prints a message if the queue is empty.

5. **`get_size(self)`**:
   - Returns the current number of elements in the queue.

6. **`has_space(self)`**:
   - Checks if there is space to add new elements.
   - Returns `True` if the `max_size` is `None` (unlimited capacity) or if the current size is less than the `max_size`.
   - Returns `False` otherwise.

7. **`is_empty(self)`**:
   - Returns `True` if the queue is empty (`size == 0`).
   - Returns `False` otherwise.

### Example Usage

The provided example code demonstrates creating a queue and performing various operations:

1. **Creating a Queue**:
   - `deli_line = Queue(10)` creates a queue with a maximum capacity of 10.

2. **Enqueuing Items**:
   - `enqueue` method adds multiple food orders to the queue.
   - If the queue reaches its maximum capacity, trying to add more items will print "Sorry, no more room!"

3. **Peeking**:
   - `peek()` shows the first item in the queue without removing it.

4. **Dequeuing Items**:
   - `dequeue` method removes and returns items from the front of the queue.
   - After dequeuing all items, trying to dequeue from an empty queue will print "The queue is totally empty!"

5. **Uncommented Code**:
   - The commented lines indicate where you can test the queue’s behavior when it’s full and when attempting to dequeue from an empty queue.

### Summary

This `Queue` class uses linked nodes to manage a collection of items efficiently with operations to add (enqueue), remove (dequeue), and inspect elements while respecting FIFO order. It also handles the queue’s size constraints and provides feedback when operations can’t be performed.
