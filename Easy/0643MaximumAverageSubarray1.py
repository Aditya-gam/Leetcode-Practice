class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Calculate the sum of the first k elements
        current_sum = sum(nums[:k])
        max_sum = current_sum

        # Slide the window across the rest of the elements
        for i in range(k, len(nums)):
            # Update the sum by subtracting the element that is sliding out and adding the new element
            current_sum += nums[i] - nums[i-k]
            # Update the max_sum if the current window's sum is greater
            if current_sum > max_sum:
                max_sum = current_sum

        # The maximum average is the maximum sum divided by k
        return max_sum / float(k)
