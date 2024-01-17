class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach 1: Sum of range - sum of nums
        length = len(nums)
        totalrangesum = (length*(length+1))/2

        return totalrangesum - sum(nums)
    
        # Approach 2: iterative Approach
        # nums.sort(reverse=True)
        # if nums[0] != len(nums):
        #     return len(nums)

        # for i in range(len(nums) - 1):
        #     if nums[i] - nums[i+1] != 1:
        #         return nums[i] - 1

        # return nums[-1] - 1 