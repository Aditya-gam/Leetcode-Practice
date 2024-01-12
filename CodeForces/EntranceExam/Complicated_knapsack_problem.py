# Input:
# The first line contains three numbers 𝑊 (1≤𝑊≤1000), which is the weight limit, 𝑛 (1≤𝑛≤100), which is the number of items, and 𝑘 (1≤𝑘≤10), which is the maximum number per item.
# The next 𝑛 lines each contains two integers. The 𝑖-th line contains 𝑤𝑖 and 𝑣𝑖.
# All 𝑤𝑖 and 𝑣𝑖 are in range 1 to 100.

def knapsack(W, n, k, items):
    """
    Calculate the maximum value that can be carried in the knapsack.

    Args:
    - W (int): Weight limit.
    - n (int): Number of items.
    - k (int): Maximum number per item.
    - items (list): List of items.

    Returns:
    - total_value (int): Maximum value that can be carried in the knapsack.
    """
    dp = [[[0 for _ in range(k + 1)] for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][0][j] = 0
    
    for w, v in items:
        for j in range(1, k + 1):
            if w <= W:
                dp[1][w][j]  = max(dp[1][w][j], v)

    for i in range(2, n + 1):
        for w in range (1, W + 1):
            for j in range(1, k + 1):
                dp[i][w][j] = dp[i - 1][w][j]
                if w >= items[i - 1][0] and j > 0:
                    dp[i][w][j] = max(dp[i][w][j], dp[i][w - items[i - 1][0]][j - 1] + items[i - 1][1])
    
    max_value = dp[n][W][k]
    return max_value   

if __name__ == "__main__":
    # Input the weight limit, number of items, and maximum number per item
    W, n, k = map(int, input().split())

    # Initialize the list of items
    items = []

    # Iterate through each item
    for _ in range(n):
        # Input the weight and value of the current item
        w, v = map(int, input().split())

        # Append the current item to the list of items
        items.append((w, v))

    total_value = knapsack(W, n, k, items)

    # Print the total value
    print(total_value)
    