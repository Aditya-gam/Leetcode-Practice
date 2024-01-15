class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # Check for empty array
        if not nums:
            return -1

        # Create a left and right pointer
        left, right = 0, len(nums) - 1

        # While the left pointer is less than or equal to the right pointer
        while left <= right:
            mid = left + (right - left) // 2

            # If the target is equal to the mid, return the mid
            if target == nums[mid]:
                return mid

            # If the target is less than the mid, set the right pointer to mid - 1
            elif target < nums[mid]:
                right = mid - 1

            # Else, set the left pointer to mid + 1
            else:
                left = mid + 1

        return -1
