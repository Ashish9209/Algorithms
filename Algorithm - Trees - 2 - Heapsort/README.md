# Heapsort Algorithm

Heapsort is a comparison-based sorting algorithm that utilizes a heap data structure to organize and sort data. It is an in-place sorting algorithm with a time complexity of \(O(n \log n)\).

## How Heapsort Works

1. **Build a Max-Heap:**
   - Convert the unordered list into a max-heap. A max-heap is a binary heap where the root node is the largest element, and each parent node is greater than its child nodes.

2. **Extract the Root:**
   - While the max-heap has at least one element, repeatedly extract the root (the largest element) of the heap.
   - Swap the root with the right-most child node of the heap.
   - Place the extracted root value at the beginning of a new list that will hold the sorted values.

3. **Rebalance the Heap:**
   - After swapping, restore the heap property by comparing the new root value with its children.
   - If the child node is greater than the parent node, swap the values.
   - Continue the rebalancing process until the heap property is restored, ensuring each parent node has a larger value than its children.

4. **Repeat:**
   - Repeat the extraction and rebalancing process until the heap is empty.

5. **Return the Sorted List:**
   - Once the heap is empty, the new list will contain the elements in sorted order.

## Steps to Implement Heapsort

1. **Insert Data into a Heap:**
   - Begin by placing the unsorted data into a heap.

2. **Extract and Swap:**
   - While the heap contains more than one element, extract the largest value from the heap by swapping it with the right-most child node and then removing the root.

3. **Restructure the Heap:**
   - After swapping, restructure the heap to maintain the heap property. Ensure that each parent node has a value greater than its child nodes.

## Summary

Heapsort is an efficient in-place sorting algorithm that organizes data using a heap data structure. It involves building a max-heap, extracting the largest elements, and rebalancing the heap until all elements are sorted. The result is a sorted list of values in ascending order.
