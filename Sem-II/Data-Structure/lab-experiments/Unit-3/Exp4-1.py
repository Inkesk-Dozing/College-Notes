import random

def bubble_sort(arr):
    a = arr.copy()  
    n = len(a)
    comparisons = 0
    swaps = 0

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        if not swapped: 
            break

    return a, comparisons, swaps


def run_experiment(size=10):
    # random input
    random_input = [random.randint(1, 100) for _ in range(size)]
    sorted_input = sorted(random_input)

    sorted_rand, comp_rand, swap_rand = bubble_sort(random_input)
    sorted_sorted, comp_sorted, swap_sorted = bubble_sort(sorted_input)

    print("Random Input:", random_input)
    print("Sorted Output:", sorted_rand)
    print("Comparisons:", comp_rand, "Swaps:", swap_rand)
    print()

    print("Already Sorted Input:", sorted_input)
    print("Sorted Output:", sorted_sorted)
    print("Comparisons:", comp_sorted, "Swaps:", swap_sorted)


if __name__ == "__main__":
    run_experiment(size=10)