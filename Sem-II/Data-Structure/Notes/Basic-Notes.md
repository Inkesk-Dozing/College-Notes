# Quick Sort

**Quick Sort** is a highly efficient, in-place sorting algorithm (average O(n log n) time, O(log n) space worst-case due to recursion stack). It uses divide-and-conquer: partition array around pivot, recursively sort subarrays.

## Quick Sort Detailed Implementation (Python)
```python
def partition(arr, low, high):
    # Choose the rightmost element as pivot
    pivot = arr[high]
    # Index of smaller element (initially shifted one position left)
    i = low - 1
    
    for j in range(low, high):
        # If current element is smaller/equal to pivot, swap with i+1
        if arr[j] <= pivot:
            i += 1  # Increment boundary of smaller elements
            arr[i], arr[j] = arr[j], arr[i]  # Swap
    
    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return pivot's final position

def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1  # Set high to end of array if not provided
    
    if low < high:
        # Partition and get pivot index
        pi = partition(arr, low, high)
        
        # Recursively sort left and right subarrays
        quick_sort(arr, low, pi - 1)   # Left side (smaller elements)
        quick_sort(arr, pi + 1, high)  # Right side (larger elements)

# Example usage and test
if __name__ == "__main__":
    test_array = [10, 7, 8, 9, 1, 5, 6, 3, 2, 4]
    print("Original:", test_array)
    quick_sort(test_array)
    print("Sorted:", test_array)
    # Output: Sorted: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## Sorting Algorithms: In-place vs Out-place

### Definitions
- **In-place Algorithm**: Modifies the input data structure directly with minimal extra space (typically O(1) auxiliary space). Elements are swapped or rearranged within the original array.
  - Pros: Space efficient, good for large datasets.
  - Cons: May destroy original order unless stable implementation.
- **Out-place (Not-in-place) Algorithm**: Requires extra space proportional to input size (O(n) auxiliary space), often using temporary arrays.
  - Pros: Can be stable, preserves original data easily.
  - Cons: Higher space usage.

### Comparison Table
| Aspect | In-place | Out-place |
|--------|----------|-----------|
| Space Complexity | O(1) | O(n) |
| Stability | Usually not (e.g., Quick Sort) | Can be (e.g., Merge Sort) |
| Examples | Quick Sort, Heap Sort, Insertion Sort | Merge Sort, Counting Sort |
| Best For | Memory-constrained environments | When extra memory available |

### Examples in C (Array-based)

#### 1. Quick Sort (In-place, O(n log n) avg time) - C Implementation
```cpp
#include <stdio.h>

void swap(int* a, int* b) {
    // Simple swap using temporary variable - constant time operation
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high) {
    // Select last element as pivot (common choice for simplicity)
    int pivot = arr[high];
    // 'i' tracks the correct position for elements <= pivot
    int i = low - 1;
    
    // Traverse from low to high-1, partition smaller elements to left
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;  // Move boundary for smaller elements
            swap(&arr[i], &arr[j]);  // Place smaller element in correct side
        }
    }
    // Finally place pivot in its sorted position
    swap(&arr[i + 1], &arr[high]);
    return i + 1;  // Pivot index
}

void quickSort(int arr[], int low, int high) {
    // Base case: single or no elements
    if (low < high) {
        int pi = partition(arr, low, high);  // Partition around pivot
        // Recurse on left half (unsorted smaller elements)
        quickSort(arr, low, pi - 1);
        // Recurse on right half (unsorted larger elements)
        quickSort(arr, pi + 1, high);
    }
}

// Usage example:
// int arr[] = {10, 7, 8, 9, 1, 5};
// quickSort(arr, 0, 5);
// Now arr is sorted!
```


#### 2. Heap Sort (In-place, O(n log n) time) - C Implementation
```cpp
#include <stdio.h>

// Heapify maintains max-heap property for subtree rooted at index 'i'
void heapify(int arr[], int n, int i) {
    int largest = i;  // Root starts as largest
    
    // Left child index
    int left = 2 * i + 1;
    // Right child index
    int right = 2 * i + 2;
    
    // Check if left child > root
    if (left < n && arr[left] > arr[largest])
        largest = left;
    
    // Check if right child > largest so far
    if (right < n && arr[right] > arr[largest])
        largest = right;
    
    // If largest not root, swap and heapify affected subtree
    if (largest != i) {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        heapify(arr, n, largest);  // Recurse down the tree
    }
}

// Main heap sort: build heap, then repeatedly extract max
void heapSort(int arr[], int n) {
    // Build max heap (rearrange array as heap)
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
    
    // Extract max elements one by one
    for (int i = n - 1; i > 0; i--) {
        // Move current root (max) to end
        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        
        // Heapify reduced heap
        heapify(arr, i, 0);
    }
}
```


#### 3. Merge Sort (Out-place, O(n log n) time, stable) - C Implementation
```cpp
#include <stdio.h>
#include <stdlib.h>

// Merges two sorted subarrays into one sorted subarray
void merge(int arr[], int l, int m, int r) {
    // Size of left and right subarrays
    int n1 = m - l + 1;
    int n2 = r - m;
    
    // Create temporary arrays (out-place space usage here)
    int* L = (int*)malloc(n1 * sizeof(int));
    int* R = (int*)malloc(n2 * sizeof(int));
    
    // Copy data to temp arrays
    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];
    
    // Merge back to original array
    int i = 0, j = 0, k = l;  // i,j for temp, k for original
    while (i < n1 && j < n2) {
        // Stable merge: <= preserves relative order of equals
        if (L[i] <= R[j]) {
            arr[k] = L[i++];
        } else {
            arr[k] = R[j++];
        }
        k++;
    }
    
    // Copy remaining elements
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
    
    free(L);
    free(R);  // Clean up temp space
}

void mergeSort(int arr[], int l, int r) {
    // Base case: 0 or 1 element already sorted
    if (l < r) {
        // Find mid and divide
        int m = l + (r - l) / 2;
        // Sort left half
        mergeSort(arr, l, m);
        // Sort right half
        mergeSort(arr, m + 1, r);
        // Merge sorted halves
        merge(arr, l, m, r);
    }
}
```


### Key Notes
- **Stability**: Merge Sort is stable; Quick/Heap Sort are not by default.
- **C Implementation Tips**: Use `malloc/free` for temp arrays in out-place. In-place avoids dynamic allocation.
- Quick Sort is already in the file header – it's in-place via partitioning/swaps.
