class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        # Calculate the initial sum of the first k elements
        current_sum = sum(nums[:k])
        max_sum = current_sum

        # Use a sliding window to update the sum efficiently
        for i in range(1, len(nums) - k + 1):
            current_sum = current_sum - nums[i - 1] + nums[i + k - 1]
            max_sum = max(max_sum, current_sum)

        return float(max_sum) / k
