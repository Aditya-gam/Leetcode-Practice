class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        
        # Binary search
        # Time complexity: O(logn)
        # Space complexity: O(1)
        start = 0
        end = len(letters) - 1
        while start <= end:
            mid = (start + end) // 2
            if letters[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1

        return letters[start % len(letters)]