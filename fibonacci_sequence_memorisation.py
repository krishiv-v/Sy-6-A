def fibonacci_memo(n, memo):
    # Base cases
    if n == 1:
        return 0

    if n == 2:
        return 1

    # Return already calculated value
    if memo[n] != -1:
        return memo[n]

    # Calculate and store the result
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)

    return memo[n]


def main():
    print("=" * 45)
    print("   FIBONACCI USING MEMOIZATION")
    print("=" * 45)

    n = int(input("Enter the value of n: "))

    if n < 1:
        print("Please enter a positive integer.")
        return

    # Create memoization array
    memo = [-1] * (n + 1)

    result = fibonacci_memo(n, memo)

    print("-" * 45)
    print(f"The {n}th Fibonacci number is: {result}")
    print("-" * 45)


if __name__ == "__main__":
    main()
