# Quick Sort

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

#### 1. Quick Sort (In-place, O(n log n) avg time)
```cpp
#include <stdio.h>

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// Usage: int arr[] = {10, 7, 8, 9, 1, 5}; quickSort(arr, 0, 5);
```

#### 2. Heap Sort (In-place, O(n log n) time)
```cpp
#include <stdio.h>

void heapify(int arr[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    if (left < n && arr[left] > arr[largest])
        largest = left;
    if (right < n && arr[right] > arr[largest])
        largest = right;
    if (largest != i) {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        heapify(arr, n, largest);
    }
}

void heapSort(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
    for (int i = n - 1; i > 0; i--) {
        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        heapify(arr, i, 0);
    }
}
```

#### 3. Merge Sort (Out-place, O(n log n) time, stable)
```cpp
#include <stdio.h>
#include <stdlib.h>

void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;
    int* L = (int*)malloc(n1 * sizeof(int));
    int* R = (int*)malloc(n2 * sizeof(int));
    for (int i = 0; i < n1; i++) L[i] = arr[l + i];
    for (int j = 0; j < n2; j++) R[j] = arr[m + 1 + j];
    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i++];
        } else {
            arr[k] = R[j++];
        }
        k++;
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
    free(L);
    free(R);
}

void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}
```

### Key Notes
- **Stability**: Merge Sort is stable; Quick/Heap Sort are not by default.
- **C Implementation Tips**: Use `malloc/free` for temp arrays in out-place. In-place avoids dynamic allocation.
- Quick Sort is already in the file header – it's in-place via partitioning/swaps.
