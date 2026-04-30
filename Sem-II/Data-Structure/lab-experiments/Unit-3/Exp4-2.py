def insertion_sort(arr, show_passes=False):
    a = arr.copy()
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        if show_passes:
            print(f"pass {i}: {a}")
    return a


if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6, 7, 1, 0, 89, 14]
    print(insertion_sort(data, show_passes=True))