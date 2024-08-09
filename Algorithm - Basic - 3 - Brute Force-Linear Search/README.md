
# Brute Force Algorithms

A **brute force** algorithm is slow but much easier to implement. It solves a problem by going through all possible choices until either a solution is found or all possibilities have been exhausted (no solution).

## Time Complexity

The time complexity of a brute force algorithm is often proportional to the input size. The Big O runtime of a brute force algorithm is \( O(N) \).

## Pros of Brute Force

- **Easier to Implement:** Brute force algorithms are simpler to code compared to more optimized algorithms.
- **Simple and Consistent:** They are straightforward, making them less prone to bugs.
- **Memory Efficiency:** Some brute force algorithms (e.g., bubble sort) may require less memory than their more optimized counterparts.

## Cons of Brute Force

- **Slow Runtime:** Performance can be poor when there are many possible choices to compute.
- **Inapplicability:** Brute force may not be practical for complex real-world problems.

# Linear Search

**Linear search** is a search algorithm that sequentially checks whether a given value is an element of a specified list by scanning the elements one-by-one until it finds the target value.

## Time Complexity

The time complexity for linear search is \( O(N) \), but its performance depends on its input:

- **Best Case:** Requires only 1 comparison if the target value is in the first position of the list.
- **Worst Case:** Requires \( N \) comparisons if the target value is in the last position of the list or does not exist.
- **Average Case:** Makes \( \frac{N}{2} \) comparisons on average.

## When to Use Linear Search

- **Target Value Near the Beginning:** Linear search is a good choice when you expect the target value to be near the start of the list.
- **Unsorted List:** It is useful for searching unsorted lists because it scans the entire list from beginning to end, regardless of order.



