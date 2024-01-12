from math import inf as INF

def make_pairs(candles):
    """
    Identify pairs of candles with the minimum difference.
    
    Args:
    - candles (list): List of candle numbers.
    
    Returns:
    - pairs (list): List of pairs with the minimum difference.
    """
    pairs = []
    min_diff = INF

    # Iterate through the candles to find pairs with minimum difference
    for i in range(len(candles) - 1):
        # Check for non-zero values to simplify the condition
        if candles[i] and candles[i + 1]:
            # Calculate the difference between consecutive candles
            diff = candles[i + 1] - candles[i]

            # Update minimum difference and reset pairs if a smaller difference is found
            if diff < min_diff:
                min_diff = diff
                pairs = [(candles[i], candles[i + 1])]
            elif diff == min_diff:
                pairs.append((candles[i], candles[i + 1]))
    
    # The function returns a list of pairs with the minimum difference
    return pairs

def minimum_difference(candles):
    """
    Calculate the minimum difference between pairs of candles.

    Args:
    - candles (list): List of candle numbers.

    Returns:
    - min_diff (int): Minimum difference between pairs.
    """
    # Check for edge cases
    if len(candles) == 1:
        return 0

    if len(candles) == 2:
        return candles[1] - candles[0]

    # Obtain pairs with minimum difference using the make_pairs function
    pairs = make_pairs(candles)

    # Initialize the minimum difference to positive infinity
    min_diff = INF

    # Iterate through pairs to find the overall minimum difference
    for pair in pairs:
        # Create a temporary list excluding the elements in the current pair
        temp = [i for i in candles if i not in pair]
        # Reverse the temporary list
        temp_reversed = temp[::-1]
        # print(pair, temp, temp_reversed) # Debugging

        # Construct num1 and num2 using the first half of the reversed and non-reversed lists
        num1 = int(str(pair[0]) + "".join(map(str, temp_reversed[:(len(candles)//2)-1])))
        num2 = int(str(pair[1]) + "".join(map(str, temp[:(len(candles)//2)-1])))

        # Calculate the current difference and update the overall minimum difference
        current_diff = num2 - num1
        min_diff = min(min_diff, current_diff)
        # print(num1, num2, current_diff, min_diff) # Debugging

    # The function returns the minimum difference between pairs
    return min_diff

if __name__ == "__main__":
    # Input the number of test cases
    t = int(input())

    # Iterate through each test case
    for _ in range(t):
        # Input the number of candles and their values
        n = int(input())
        candles = list(map(int, input().split()))

        # Output the minimum difference for the current test case
        print(minimum_difference(candles))
