class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in nums:
                count = 1
                curr = num + 1

                while curr in nums:
                    count += 1
                    curr += 1

                res = max(res, count)

        return res
