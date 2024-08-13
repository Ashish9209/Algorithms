
Bucket sort is a sorting algorithm designed to sort elements by distributing them into different "buckets" or groups based on their value. It’s particularly useful when dealing with uniformly distributed data over a range. Here’s a step-by-step explanation of how it works:

1. **Create Buckets:** Divide the range of the data into a number of buckets. The number of buckets can be predetermined based on the expected range of the data and how fine-grained you want the sorting to be.

2. **Distribute Elements:** Place each element of the array into one of the buckets based on its value. For example, if you have a set of integers from 1 to 100, you might use buckets to cover ranges like 1-10, 11-20, and so on.

3. **Sort Buckets Individually:** Sort the elements within each bucket. This can be done using any other sorting algorithm, like insertion sort or quicksort. Because the range within each bucket is smaller, sorting within each bucket is generally more efficient.

4. **Concatenate Buckets:** After all the buckets are sorted individually, concatenate them in order. The result will be a fully sorted array.


### Characteristics

- **Time Complexity:** The average time complexity of bucket sort is \(O(n + k)\), where \(n\) is the number of elements and \(k\) is the number of buckets. This can be very efficient if the data is uniformly distributed and the number of buckets is chosen wisely.
- **Space Complexity:** Bucket sort requires additional space for the buckets, so its space complexity is \(O(n + k)\).
- **Stability:** Bucket sort is stable if the sorting algorithm used for individual buckets is stable.

### Limitations

- **Distribution Assumption:** The efficiency of bucket sort assumes that the data is uniformly distributed. If the data is not uniformly distributed, the buckets might not be evenly populated, leading to inefficiencies.
- **Overhead:** There’s some overhead involved in creating and managing buckets, which might not be worthwhile for smaller data sets or if the data distribution is not suitable for bucket sorting.

Overall, bucket sort is a useful algorithm for specific cases, especially when dealing with large amounts of data that fit well within the assumptions of the algorithm.
