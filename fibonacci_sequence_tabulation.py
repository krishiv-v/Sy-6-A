def fibonacci_tabulation(n):
    # Base cases
    if n == 1:
        return 0

    if n == 2:
        return 1

    # Create DP table
    fib = [0] * (n + 1)

    # Initialize first two values
    fib[1] = 0
    fib[2] = 1

    # Fill the table
    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


def main():
    print("=" * 45)
    print("   FIBONACCI USING TABULATION")
    print("=" * 45)

    n = int(input("Enter the value of n: "))

    if n < 1:
        print("Please enter a positive integer.")
        return

    result = fibonacci_tabulation(n)

    print("-" * 45)
    print(f"The {n}th Fibonacci number is: {result}")
    print("-" * 45)


if __name__ == "__main__":
    main()
