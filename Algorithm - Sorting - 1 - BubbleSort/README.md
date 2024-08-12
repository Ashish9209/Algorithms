
This code snippet demonstrates two variations of the bubble sort algorithm for sorting a list of integers in ascending order. It also compares the performance of these two variations by counting the number of iterations they perform. Here’s a breakdown of the code and its functionality:

### Initial Setup

```python
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("PRE SORT: {0}".format(nums))
```
- **`nums`**: A list of integers in descending order.
- **`print("PRE SORT: {0}".format(nums))`**: Prints the list before sorting.

### Swap Function

```python
def swap(arr, index_1, index_2):
  temp = arr[index_1]
  arr[index_1] = arr[index_2]
  arr[index_2] = temp
```
- **`swap(arr, index_1, index_2)`**: Swaps the elements at `index_1` and `index_2` in the list `arr`.

### Unoptimized Bubble Sort

```python
def bubble_sort_unoptimized(arr):
  iteration_count = 0
  for el in arr:
    for index in range(len(arr) - 1):
      iteration_count += 1
      if arr[index] > arr[index + 1]:
        swap(arr, index, index + 1)

  print("PRE-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))
```
- **`bubble_sort_unoptimized(arr)`**: An unoptimized version of the bubble sort algorithm.
  - **Outer Loop**: Iterates through each element of the array.
  - **Inner Loop**: Iterates through the array, comparing adjacent elements.
    - If an element is greater than the next one, it swaps them using the `swap` function.
  - **`iteration_count`**: Counts the total number of comparisons made.
  - **`print("PRE-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))`**: Prints the iteration count for this unoptimized version.

### Optimized Bubble Sort

```python
def bubble_sort(arr):
  iteration_count = 0
  for i in range(len(arr)):
    # iterate through unplaced elements
    for idx in range(len(arr) - i - 1):
      iteration_count += 1
      if arr[idx] > arr[idx + 1]:
        # replacement for swap function
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
        
  print("POST-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))
```
- **`bubble_sort(arr)`**: An optimized version of the bubble sort algorithm.
  - **Outer Loop**: Runs `len(arr)` times, where `i` is the current pass number.
    - **Inner Loop**: Iterates through the list but reduces the range by `i` on each pass (since the largest elements bubble to the end of the list with each pass).
    - **`arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]`**: Swaps elements if the current element is greater than the next one, without using the separate `swap` function.
  - **`iteration_count`**: Counts the total number of comparisons made.
  - **`print("POST-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))`**: Prints the iteration count for this optimized version.

### Function Calls and Final Output

```python
bubble_sort_unoptimized(nums.copy())
bubble_sort(nums)
print("POST SORT: {0}".format(nums))
```
- **`bubble_sort_unoptimized(nums.copy())`**: Runs the unoptimized bubble sort on a copy of the `nums` list and prints the iteration count.
- **`bubble_sort(nums)`**: Runs the optimized bubble sort on the original `nums` list and prints the iteration count.
- **`print("POST SORT: {0}".format(nums))`**: Prints the sorted list after running the optimized bubble sort.

### Summary of Key Points

1. **Bubble Sort Overview**:
   - Bubble sort is a simple comparison-based sorting algorithm.
   - It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

2. **Unoptimized Bubble Sort**:
   - Runs the inner loop for each element in the list, leading to a higher number of comparisons.
   - Always performs `n-1` comparisons for each element, resulting in a time complexity of \(O(n^2)\).

3. **Optimized Bubble Sort**:
   - Reduces the number of comparisons by not checking the last `i` elements in each pass, as they are already sorted.
   - Still has a time complexity of \(O(n^2)\) in the worst case, but performs fewer comparisons than the unoptimized version.

4. **Performance Comparison**:
   - The iteration counts will be different between the unoptimized and optimized versions, with the optimized version generally performing fewer comparisons. 

This code demonstrates how minor improvements in the bubble sort algorithm can lead to performance gains by reducing the number of unnecessary comparisons.

