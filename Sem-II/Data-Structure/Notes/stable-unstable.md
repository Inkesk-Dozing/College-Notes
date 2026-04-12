# Stable vs Unstable Sorting Algorithms

## Definitions
- **Stable Sort**: Preserves the **relative order** of equal elements in the input. If two items have the same key (value), their original order is maintained in the sorted output.
  - Important when sorting by multiple criteria (e.g., sort by grade, then by name stably).
- **Unstable Sort**: Does **not** guarantee preservation of relative order for equal elements. Order of equals may change arbitrarily.

## Why It Matters
- **Stable**: Safe for multi-level sorts, maintains data integrity.
- **Unstable**: Often faster/practical but can reorder equals.

## Comparison Table
| Property | Stable Examples | Unstable Examples |
|----------|-----------------|-------------------|
| Algorithms | Merge Sort, Insertion Sort, Bubble Sort, Counting Sort (if implemented stably) | Quick Sort, Heap Sort, Selection Sort |
| Space | Usually O(n) (out-place) | Often O(1) (in-place) |
| Use Case | Sorting records with secondary keys | Pure numerical sorts where order irrelevant |
| Speed | Slightly slower due to stability checks | Generally faster |

## Visual Example
**Input Array** (with indices for equal elements): `[(4, 'B'), (1, 'A'), (4, 'C'), (3, 'D'), (1, 'E')]`

### Stable Sort (e.g., Merge Sort)
```
Sorted by value: [(1, 'A'), (1, 'E'), (3, 'D'), (4, 'B'), (4, 'C')]
Note: 4-B before 4-C preserved!
```

### Unstable Sort (e.g., Quick Sort)
```
Sorted by value: [(1, 'A'), (1, 'E'), (3, 'D'), (4, 'C'), (4, 'B')]
Note: 4-C now before 4-B (order changed)!
```

## Python Examples (Runnable)

### 1. Stable: Merge Sort (Python's `sorted()` is stable Timsort)
```python
# Data with duplicates
data = [(4, 'B'), (1, 'A'), (4, 'C'), (3, 'D'), (1, 'E')]

print("Original:", data)
sorted_stable = sorted(data, key=lambda x: x[0])  # Stable sort by first element
print("Stable sorted:", sorted_stable)
# Output preserves 'B' before 'C' for value 4
```

### 2. Unstable: Quick Sort Implementation
```python
def quick_partition(arr, low, high):
    pivot = arr[high][0]  # Pivot by first element
    i = low - 1
    for j in range(low, high):
        if arr[j][0] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_unstable(arr, low=0, high=None):
    if high is None: high = len(arr) - 1
    if low < high:
        pi = quick_partition(arr, low, high)
        quick_sort_unstable(arr, low, pi - 1)
        quick_sort_unstable(arr, pi + 1, high)

# Same data
data = [(4, 'B'), (1, 'A'), (4, 'C'), (3, 'D'), (1, 'E')]
print("Original:", data)
quick_sort_unstable(data)
print("Unstable sorted:", data)
# Output: Order of equal elements (4's) may swap!
```

## C Examples
### Stable: Modified Bubble Sort (simple stable implementation)
```c
void bubbleSortStable(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {  // > ensures stability
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}
```

### Unstable: Quick Sort (as in Basic-Notes.md)

## Key Takeaways
- **Stable sorts are crucial** for real-world data with ties/secondary sorting.
- Most in-place sorts are unstable; out-place can be made stable.
- Python's `sorted()` and `list.sort()` are **stable** (Timsort).
- Test stability with duplicate keys + indices!
