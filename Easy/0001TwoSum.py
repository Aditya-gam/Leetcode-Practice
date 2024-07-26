class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i

        return []

    def twoSum2(self, nums, target):

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []

    def twoSum3(self, nums, target):

        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                return [i, nums.index(target - nums[i], i+1)]

        return []
