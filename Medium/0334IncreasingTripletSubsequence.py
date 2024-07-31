class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        first = second = float("inf")

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False

    # Time complexity: O(n^2): Gives TLE
    def increasingTriplet1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)

        if n < 3:
            return False

        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

                if dp[i] >= 3:
                    return True

        return False
