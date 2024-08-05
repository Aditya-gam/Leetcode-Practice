class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        # Create a dictionary to store the count of each character in word1
        count1 = {}

        # Iterate through word1 and store the count of each character in the dictionary
        for char in word1:
            if char in count1:
                count1[char] += 1
            else:
                count1[char] = 1

        # Create a dictionary to store the count of each character in word2
        count2 = {}

        # Iterate through word2 and store the count of each character in the dictionary
        for char in word2:
            if char in count2:
                count2[char] += 1
            else:
                count2[char] = 1

        # Create a set to store the unique counts of characters in word1
        unique_counts1 = set()

        # Iterate through the dictionary and add the count of each character to the set
        for key in count1:
            unique_counts1.add(count1[key])

        # Create a set to store the unique counts of characters in word2
        unique_counts2 = set()

        # Iterate through the dictionary and add the count of each character to the set
        for key in count2:
            unique_counts2.add(count2[key])

        # If the unique counts of characters in word1 and word2 are not equal, return False
        if unique_counts1 != unique_counts2:
            return False

        # Create a set to store the unique characters in word1
        unique_chars1 = set(word1)

        # Create a set to store the unique characters in word2
        unique_chars2 = set(word2)

        # If the unique characters in word1 and word2 are not equal, return False
        if unique_chars1 != unique_chars2:
            return False

        # Sort the counts of characters in word1 and word2
        sorted_counts1 = sorted(count1.values())
        sorted_counts2 = sorted(count2.values())

        # If the sorted counts of characters in word1 and word2 are not equal, return False
        if sorted_counts1 != sorted_counts2:
            return False

        # Otherwise, return True
        return True
