The code implements the Merge Sort algorithm, which is a popular and efficient sorting algorithm based on the divide-and-conquer principle. Here’s a detailed explanation of the code and how it works:

### Merge Sort Overview

Merge Sort is a comparison-based sorting algorithm that divides the input list into two halves, recursively sorts each half, and then merges the sorted halves back together. It has a time complexity of \(O(n \log n)\) in the worst case, making it suitable for large datasets.

### Code Breakdown

#### 1. `merge_sort` Function

```python
def merge_sort(items):
  if len(items) <= 1:
    return items

  middle_index = len(items) // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]

  left_sorted = merge_sort(left_split)
  right_sorted = merge_sort(right_split)

  return merge(left_sorted, right_sorted)
```

- **Base Case**:
  - If the list `items` has 1 or 0 elements (`len(items) <= 1`), it is already sorted, so it returns the list as is.

- **Divide**:
  - The list `items` is split into two halves:
    - `left_split`: Contains elements from the start up to the middle index.
    - `right_split`: Contains elements from the middle index to the end.

- **Recursive Sort**:
  - The `merge_sort` function is called recursively on both halves (`left_split` and `right_split`) to sort them.

- **Merge**:
  - The `merge` function is called to combine the two sorted halves into a single sorted list.

#### 2. `merge` Function

```python
def merge(left, right):
  result = []

  while (left and right):
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)

  if left:
    result += left
  if right:
    result += right

  return result
```

- **Initialization**:
  - `result`: An empty list that will store the merged and sorted elements.

- **Merge Process**:
  - The `while` loop continues as long as both `left` and `right` lists are not empty.
  - **Comparison**: The first elements of both lists are compared. The smaller element is appended to `result`, and the corresponding list has its first element removed (`pop(0)`).

- **Append Remaining Elements**:
  - After the `while` loop, one of the lists may still have remaining elements.
  - If `left` is not empty, its elements are appended to `result`.
  - If `right` is not empty, its elements are appended to `result`.

- **Return**:
  - The merged and sorted `result` list is returned.

#### 3. Testing the Merge Sort

```python
unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]
unordered_list2 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]
unordered_list3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]

ordered_list1 = merge_sort(unordered_list1)
ordered_list2 = merge_sort(unordered_list2)
ordered_list3 = merge_sort(unordered_list3)

print(ordered_list1, ordered_list2, ordered_list3)
```

- **Define Lists**:
  - `unordered_list1`, `unordered_list2`, and `unordered_list3` are lists of integers that need to be sorted.

- **Sort Lists**:
  - `merge_sort` is called on each unordered list to produce `ordered_list1`, `ordered_list2`, and `ordered_list3`, which are sorted versions of the original lists.

- **Print Results**:
  - The sorted lists are printed to the console.

### Points of Note

- **Efficiency**:
  - The merge function repeatedly pops elements from the front of the lists, which can be inefficient because `pop(0)` has a time complexity of \(O(n)\). For improved performance, using a queue or index-based approach would be better.

- **Usage**:
  - The `merge_sort` function is well-suited for larger datasets and scenarios where stable sorting is needed, as it maintains the relative order of equal elements.

Overall, the code provides a clear and functional implementation of the Merge Sort algorithm, demonstrating its divide-and-conquer approach to sorting.