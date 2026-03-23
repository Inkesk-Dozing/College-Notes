def complexity_drill(n):
    # Snippet 1: Single Loop - O(n)
    count_linear = 0
    for i in range(n):
        count_linear += 1
    print(f"Linear Loop (n={n}): {count_linear} operations")
    #  The loop iterates exactly n times, where each operation takes constant time
    # As input n grows, the execution time grows at the same linear rate
    # Hence, Time Complexity is O(n)

    # Snippet 2: Triangular Loop - O(n^2)
    count_nested = 0
    for i in range(n):
        for j in range(n):
            count_nested += 1
    print(f"Nested Loop (n={n}): {count_nested} operations")
    # For every iteration of the outer loop (n), the inner loop runs n times 
    # The total operations are n * n = n^2, representing quadratic growth
    # Hence, time complexity is O(n*n) = O(n^2)
    
    # Snippet 3: Triangular Loop - O(n^2)
    count_tri = 0
    for i in range(n):
        for j in range(i, n):
            count_tri += 1
    print(f"Triangular Loop (n={n}): {count_tri} operations")
    # The inner loop runs n, n-1, ..., 1 times, totaling [n*(n+1)]/2 operations 
    # Since the highest order term is n^2, the complexity remains O(n^2)
    # Hence, time complexity is O(n^2)

    # Snippet 4: Halving Loop - O(log n)
    count_log = 0
    nn = n
    while nn > 1:
        nn //= 2
        count_log += 1
    print(f"Halving Loop (n={n}): {count_log} operations")
    # The input size is divided by 2 in each iteration until it reaches 1 
    # The number of steps required to reach 1 is the definition of log_2(n)
    # Hence, time complexity is O(logn)
    
def main():
    n = int(input("Enter a positive integer: "))
    complexity_drill(n)
    
if __name__ == "__main__":
    main()