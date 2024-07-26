class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        max_len = max(len(word1), len(word2))
        result = []
        for i in range(max_len):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])

        return "".join(result)

    def mergeAlternately2(self, word1, word2):
        min_len = min(len(word1), len(word2))
        res = ''

        for i in range(0, min_len):
            res += word1[i]
            res += word2[i]

        res += word1[min_len:] + word2[min_len:]

        return res
