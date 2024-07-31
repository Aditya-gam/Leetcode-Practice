class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        res = [1] * n
        left = 1
        right = 1

        for i in range(n):
            res[i] *= left
            left *= nums[i]
            res[n - 1 - i] *= right
            right *= nums[n - 1 - i]

        return res

    def productExceptSelf1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        res = [1] * n

        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        right = 1

        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res
