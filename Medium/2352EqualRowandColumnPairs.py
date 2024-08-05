class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        n = len(grid)

        row_count = defaultdict(int)
        col_count = defaultdict(int)

        # Count rows
        for row in grid:
            row_count[tuple(row)] += 1

        # Count columns
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            col_count[col] += 1

        # Calculate the number of equal pairs
        equal_pairs = 0
        for key in row_count:
            if key in col_count:
                equal_pairs += row_count[key] * col_count[key]

        return equal_pairs
