class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False
        s_index = 0
        for t_index in range(len(t)):
            if s_index == len(s):
                return True
            if s[s_index] == t[t_index]:
                s_index += 1

        return s_index == len(s)
