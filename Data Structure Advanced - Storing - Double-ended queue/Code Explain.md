Here's a simple explanation of the `Deque` class code:

```python
class Deque:
  def __init__(self):
    self.elements = []
```
- **`__init__` Method**: Initializes an empty list `elements` to store the items in the deque.

```python
  def add_first(self, item):
    self.elements.append(item)
```
- **`add_first` Method**: Adds an item to the front of the deque by appending it to the end of the list (the front is represented as the end of the list in this implementation).

```python
  def add_last(self, item):
    self.elements.insert(0, item)
```
- **`add_last` Method**: Adds an item to the end of the deque by inserting it at the beginning of the list.

```python
  def remove_first(self):
    item = self.elements.pop()
    return item
```
- **`remove_first` Method**: Removes and returns the item from the front of the deque (which is the last item in the list due to the way `add_first` was implemented).

```python
  def remove_last(self):
    item = self.elements.pop(0)
    return item
```
- **`remove_last` Method**: Removes and returns the item from the end of the deque (which is the first item in the list).

```python
  def is_empty(self):
    if len(self.elements) > 0:
      return False
    return True
```
- **`is_empty` Method**: Checks if the deque is empty. Returns `True` if the list is empty, otherwise `False`.

```python
  def size(self):
    return len(self.elements)
```
- **`size` Method**: Returns the number of items in the deque.

```python
  def peek_first(self):
    return self.elements[-1]
```
- **`peek_first` Method**: Returns the item at the front of the deque without removing it (the last item in the list).

```python
  def peek_last(self):
    return self.elements[0]
```
- **`peek_last` Method**: Returns the item at the end of the deque without removing it (the first item in the list).

```python
  def display_deque(self):
    print('\t | \t'.join(str(item) for item in self.elements))
```
- **`display_deque` Method**: Prints all the items in the deque, separated by tabs.

### Example Usage

```python
deque = Deque()
deque.add_first(5)
deque.add_first(20)
deque.add_last(42)
popped_front = deque.remove_first()
print("Popped value: " + str(popped_front))  # Output: Popped value: 20
popped_rear = deque.remove_last()
print("Popped value: " + str(popped_rear))  # Output: Popped value: 42

# Test deque methods
print(deque.is_empty())  # Output: False
print(deque.size())  # Output: 1
deque.remove_first()
print(deque.is_empty())  # Output: True
print(deque.size())  # Output: 0
deque.display_deque()  # Output: (prints nothing as the deque is empty)
```

**Summary**: The `Deque` class allows you to add and remove elements from both ends of the deque. The methods include adding to the front or end, removing from the front or end, checking if the deque is empty, and getting the size of the deque.
