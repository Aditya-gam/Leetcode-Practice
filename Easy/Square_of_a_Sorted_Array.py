class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Two pointers
        # Time complexity: O(n)
        # Space complexity: O(n)
        res = [0] * len(nums)
        start = 0
        end = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[start]) > abs(nums[end]):
                res[i] = nums[start] ** 2
                start += 1
            else:
                res[i] = nums[end] ** 2
                end -= 1

        return res