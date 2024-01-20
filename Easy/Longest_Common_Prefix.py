class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        res = ""

        if not strs:
            return res

        # Iterate through the characters of the first string
        for i in range(len(strs[0])):
            # Iterate through the strings
            for j in range(1, len(strs)):
                # If the current character of the first string is not equal to the current character of the current string, return the result
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return res
            # Else add the current character to the result
            res += strs[0][i]

        # Return the result
        return res
