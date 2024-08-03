class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = 0
        max_length = 0
        num_zeroes = 0

        while right < len(nums):
            if nums[right] == 0:
                num_zeroes += 1

            while num_zeroes > 1:
                if nums[left] == 0:
                    num_zeroes -= 1
                left += 1

            max_length = max(max_length, right - left)
            right += 1

        return max_length
    
    def longestSubarray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Time: O(N) Space: O(1)
        left = 0
        right = 0
        num_zeroes = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                num_zeroes += 1

            if num_zeroes > 1:
                if nums[left] == 0:
                    num_zeroes -= 1
                left += 1

        return right - left