class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = s.split()
        i, j = 0, len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return " ".join(s)

    def reverseWords1(self, s):
        """
        :type s: str
        :rtype: str
        """

        return " ".join(s.split()[::-1])

    def reverseWords2(self, s):
        """
        :type s: str
        :rtype: str
        """

        return " ".join(reversed(s.split()))
