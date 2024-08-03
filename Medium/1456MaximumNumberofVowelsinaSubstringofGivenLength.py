class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        vowels = set(['a', 'e', 'i', 'o', 'u'])
        current_vowels = sum(1 for i in range(k) if s[i] in vowels)
        max_vowels = current_vowels

        for i in range(k, len(s)):
            current_vowels += (s[i] in vowels) - (s[i - k] in vowels)
            max_vowels = max(max_vowels, current_vowels)

        return max_vowels
