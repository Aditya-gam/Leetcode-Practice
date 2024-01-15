class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # Approach: Sliding Window
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # Edge Case
        if not prices:
            return 0
        
        # Initialize Variables
        max_profit = 0
        min_price = prices[0]

        # Iterate through prices
        for i in range(1, len(prices)):
            # Update min_price
            if prices[i] < min_price:
                min_price = prices[i]
            # Update max_profit
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit