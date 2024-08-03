class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # Count the number of zeroes
        num_zeroes = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                num_zeroes += 1

        # Remove zeroes from the list
        for i in range(num_zeroes):
            nums.remove(0)

        # Add zeroes to the end of the list
        for i in range(num_zeroes):
            nums.append(0)

        return nums

    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0

        for current_index in range(len(nums)):
            if nums[current_index] != 0:
                nums[non_zero_index], nums[current_index] = nums[current_index], nums[non_zero_index]
                non_zero_index += 1

        return nums
