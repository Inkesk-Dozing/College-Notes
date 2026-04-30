import random
import time

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def merge(left, right):
    i = j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

import random

def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low=0, high=None):
    if high is None:
        arr = arr.copy()
        high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

def time_func(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return end - start

def generate_datasets(size, seed):
    random.seed(seed)
    rand = [random.randint(1, 100000) for _ in range(size)]
    sorted_data = sorted(rand)
    reverse_data = sorted_data[::-1]
    return rand, sorted_data, reverse_data

def run_experiment(sizes, seed):
    print(f"{'Size':>6} | {'Type':>8} | {'Insertion':>10} | {'Merge':>10} | {'Quick':>10}")
    print("-" * 60)
    for size in sizes:
        rand, sorted_data, reverse_data = generate_datasets(size, seed)
        datasets = [("Random", rand), ("Sorted", sorted_data), ("Reverse", reverse_data)]
        for dtype, data in datasets:
            t_ins = time_func(insertion_sort, data)
            t_merge = time_func(merge_sort, data)
            t_quick = time_func(quick_sort, data)
            print(f"{size:6} | {dtype:8} | {t_ins:10.6f} | {t_merge:10.6f} | {t_quick:10.6f}")

if __name__ == "__main__":
    run_experiment([1000, 5000, 10000], seed=42)