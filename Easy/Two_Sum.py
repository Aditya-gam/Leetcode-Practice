class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Method 3: Two Pointers
        # Time Complexity: O(nlogn)
        # Space Complexity: O(n)
        nums = [(nums[i], i) for i in range(len(nums))]
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left][0] + nums[right][0] == target:
                return [nums[left][1], nums[right][1]]
            elif nums[left][0] + nums[right][0] < target:
                left += 1
            else:
                right -= 1
        
        return [-1, -1]