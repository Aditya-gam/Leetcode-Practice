class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        num_operations = 0
        num_dict = {}

        for num in nums:
            if k - num in num_dict and num_dict[k - num] > 0:
                num_operations += 1
                num_dict[k - num] -= 1
            else:
                num_dict[num] = num_dict.get(num, 0) + 1

        return num_operations
