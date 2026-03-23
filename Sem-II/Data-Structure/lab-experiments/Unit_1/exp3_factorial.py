def factorial(n):
    if n < 0:
        return "Invalid"
    elif n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
def main():
    n = int(input("Enter a positive integer: "))
    fact = factorial(n)
    print(f"Factorial of {n} is {fact}")
    
if __name__ == "__main__":
    main()