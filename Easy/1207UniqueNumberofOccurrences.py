class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        # Create a dictionary to store the count of each element in the array
        count = {}

        # Iterate through the array and store the count of each element in the dictionary
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # Create a set to store the unique counts
        unique_counts = set()

        # Iterate through the dictionary and add the count of each element to the set
        for key in count:
            unique_counts.add(count[key])

        # If the length of the set is equal to the length of the dictionary, return True
        # Otherwise, return False
        return len(unique_counts) == len(count)
