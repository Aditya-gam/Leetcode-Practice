from collections import defaultdict

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        count = defaultdict(int)

        for char in s:
            count[char] += 1

        for char in t:
            count[char] -= 1
            if count[char] < 0:
                return False

        return True
