def fib_naive(n):
    global naivecalls
    naivecalls += 1 
    if n <= 1:
            return n
    else:
        return fib_naive(n-1) + fib_naive(n-2)


def fib_memo_util(n, memo):
    global memocalls
    memocalls += 1
    if n <= 1:
        return n
    if memo[n] != -1:
        return memo[n]
    memo[n] = fib_memo_util(n - 1, memo) + fib_memo_util(n - 2, memo)
    return memo[n]

# Wrapper Function
def fib_memo(n):
    memo = [-1] * (n + 1)
    return fib_memo_util(n, memo)

naivecalls = 0
memocalls = 0

def main():
    n = int(input("Enter a positive integer: "))
    print(f"{n}th term of fibonacci series using naive approach: {fib_naive(n)}")
    print(f"Naive calls: {naivecalls}")
    print(f"{n}th term of fibonacci series using memoized approach: {fib_memo(n)}")
    print(f"Memoized calls: {memocalls}")
    
if __name__ == "__main__":
    main()