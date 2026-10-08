def knapsack_bottom_up(weights, values, capacity):
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        for j in range(capacity, weights[i] - 1, -1):
            dp[j] = max(dp[j], values[i] + dp[j - weights[i]])

    return dp[capacity]


def knapsack_top_down(weights, values, capacity, memo=None):
    if memo is None:
        memo = {}

    if capacity == 0 or not weights:
        return 0

    key = (len(weights), capacity)

    if key in memo:
        return memo[key]

    if weights[-1] > capacity:
        ans = knapsack_top_down(weights[:-1], values[:-1], capacity, memo)
    else:
        ans = max(
            values[-1] + knapsack_top_down(
                weights[:-1], values[:-1], capacity - weights[-1], memo
            ),
            knapsack_top_down(weights[:-1], values[:-1], capacity, memo)
        )

    memo[key] = ans
    return ans


# Input
n = int(input("Number of items: "))
weights = list(map(int, input("Weights: ").split()))
values = list(map(int, input("Values: ").split()))
capacity = int(input("Capacity: "))

print("Bottom-Up:", knapsack_bottom_up(weights, values, capacity))
print("Top-Down:", knapsack_top_down(weights, values, capacity))
