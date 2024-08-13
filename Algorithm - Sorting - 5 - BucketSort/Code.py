
def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    
    # Find the maximum value in the array
    max_value = max(arr)
    min_value = min(arr)
    
    # Create empty buckets
    bucket_count = len(arr)  # Number of buckets
    buckets = [[] for _ in range(bucket_count)]
    
    # Define the range of values each bucket will hold
    bucket_range = (max_value - min_value + 1) / bucket_count
    
    # Distribute elements into buckets
    for num in arr:
        index = int((num - min_value) / bucket_range)
        if index == bucket_count:  # Handle the case where num == max_value
            index -= 1
        buckets[index].append(num)
    
    # Sort individual buckets and concatenate results
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    
    return sorted_arr

# Example usage
arr = [29, 25, 3, 49, 9, 37, 21, 43]
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)
