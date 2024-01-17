class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach 1: Using XOR
        # a ^ a = 0
        # a ^ 0 = a
        # a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        res = 0
        for num in nums:
            res ^= num

        return res

        # Approach 2: Using Counter
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # from collections import Counter
        # count = Counter(nums)
        # for key, value in count.items():
        #     if value == 1:
        #         return key

        # Approach 3: Using Math
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # return 2 * sum(set(nums)) - sum(nums)
