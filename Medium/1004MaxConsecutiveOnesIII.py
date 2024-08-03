class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left = 0
        right = 0
        max_ones = 0
        num_zeroes = 0

        while right < len(nums):
            if nums[right] == 0:
                num_zeroes += 1

            while num_zeroes > k:
                if nums[left] == 0:
                    num_zeroes -= 1
                left += 1

            max_ones = max(max_ones, right - left + 1)
            right += 1

        return max_ones

    def longestOnes2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Time: O(N) Space: O(1)
        left = 0
        right = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1

            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

        return right - left + 1
