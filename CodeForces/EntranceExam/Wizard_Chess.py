def find_minimum_moves(start, end, occupied):
    """
    Function to find the minimum number of moves required by the knight to reach the destination square
    :param start: The starting square
    :param end: The destination square
    :param occupied: List of occupied squares
    :return: The minimum number of moves required by the knight to reach the destination square
    """
    # If the starting square is the same as the destination square, return 0
    if start == end:
        return 0

    # If the starting square is in the list of occupied squares, return -1
    if start in occupied:
        return -1

    # If the destination square is in the list of occupied squares, return -1
    if end in occupied:
        return -1

    

if __name__ == "__main__":
    i = 1
    while True:
        n = int(input())
        if n == -1:
            break
        i += 1
        # Input the positions of the occupied squares
        occupied = []
        for _ in range(n):
            occupied.append(tuple(map(int, input().split())))

        # Input the position of the starting square and the destination square
        start, end = tuple(map(int, input().split()))

        # Call the function to find the minimum number of moves required by the knight to reach the destination square
        minimum_moves = find_minimum_moves(start, end, occupied)

        print(f'Board {i}: {minimum_moves} moves required.' if minimum_moves != -1 else f'Board {i}: not reachable.')
