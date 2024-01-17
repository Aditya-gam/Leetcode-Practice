class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Approach 1: Using set iterative Approach
        nums_set = set(nums)
        res = []

        for i in range(1, len(nums)+1):
            if i not in nums_set:
                res.append(i)

        return res
    
        # Approach 2: Using set 
        # return list(set(range(1, len(nums)+1)) - set(nums))
    
        
        