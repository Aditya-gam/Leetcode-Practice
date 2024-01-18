class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Solution 1: Use a dictionary to store the count of each element
        # Time: O(n)
        # Space: O(n)
        # count = {}
        # for num in nums:
        #     if num not in count:
        #         count[num] = 1
        #     else:
        #         count[num] += 1
        # for key, value in count.items():
        #     if value > len(nums) / 2:
        #         return key

        # Solution 2: Sort the list and return the middle element
        # Time: O(nlogn)
        # Space: O(1)
        # nums.sort()
        # return nums[len(nums) / 2]

        # Solution 3: Boyer-Moore Voting Algorithm
        # Time: O(n)
        # Space: O(1)
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            if candidate == num:
                count += 1
            else:
                count -= 1
        return candidate
