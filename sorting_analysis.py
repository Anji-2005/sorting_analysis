import random
import time
import math


# -------------------------------
# Heap Sort
# -------------------------------

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]

        # Restore heap property
        heapify(arr, i, 0)

    return arr


# -------------------------------
# Merge Sort
# -------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# -------------------------------
# Quick Sort
# -------------------------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    right = []

    for i in range(len(arr) - 1):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


# -------------------------------
# Function to Measure Time
# -------------------------------
def measure_sorting_time(sort_function, arr):
    start_time = time.perf_counter()
    sorted_arr = sort_function(arr.copy())
    end_time = time.perf_counter()

    time_taken = end_time - start_time
    return sorted_arr, time_taken


# -------------------------------
# Main Program
# -------------------------------
n = 100
trials = 10

heap_times = []
merge_times = []
quick_times = []

for trial in range(trials):
    # Step 1: Create random array of size 100
    original_array = [random.randint(1, 1000) for _ in range(n)]

    # Step 2: Make 3 copies of the same array
    arr1 = original_array.copy()
    arr2 = original_array.copy()
    arr3 = original_array.copy()

    # Step 3: Run Heap Sort, Merge Sort, Quick Sort
    heap_result, heap_time = measure_sorting_time(heap_sort, arr1)
    merge_result, merge_time = measure_sorting_time(merge_sort, arr2)
    quick_result, quick_time = measure_sorting_time(quick_sort, arr3)

    # Step 4: Compare the results
    if heap_result == merge_result == quick_result:
        print(f"Trial {trial + 1}: All sorting results match.")
    else:
        print(f"Trial {trial + 1}: Sorting results do NOT match.")

    # Store times
    heap_times.append(heap_time)
    merge_times.append(merge_time)
    quick_times.append(quick_time)


# -------------------------------
# Function to Calculate Statistics
# -------------------------------
def calculate_statistics(times, n):
    avg_time = sum(times) / len(times)
    min_time = min(times)
    max_time = max(times)

    n_log_n = n * math.log2(n)

    avg_constant = avg_time / n_log_n
    min_constant = min_time / n_log_n
    max_constant = max_time / n_log_n

    return avg_time, min_time, max_time, avg_constant, min_constant, max_constant


# -------------------------------
# Calculate Stats for Each Sort
# -------------------------------
heap_stats = calculate_statistics(heap_times, n)
merge_stats = calculate_statistics(merge_times, n)
quick_stats = calculate_statistics(quick_times, n)


# -------------------------------
# Print Final Results
# -------------------------------
print("\nFinal Comparison")
print("-" * 80)

print("Algorithm\tAverage Time\t\tMinimum Time\t\tMaximum Time\t\tAverage Constant")
print("-" * 80)

print(f"Heap Sort\t{heap_stats[0]:.10f}\t\t{heap_stats[1]:.10f}\t\t{heap_stats[2]:.10f}\t\t{heap_stats[3]:.15f}")
print(f"Merge Sort\t{merge_stats[0]:.10f}\t\t{merge_stats[1]:.10f}\t\t{merge_stats[2]:.10f}\t\t{merge_stats[3]:.15f}")
print(f"Quick Sort\t{quick_stats[0]:.10f}\t\t{quick_stats[1]:.10f}\t\t{quick_stats[2]:.10f}\t\t{quick_stats[3]:.15f}")