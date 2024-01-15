class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = s.lower()
        s = ''.join(e for e in s if e.isalnum())

        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False

        # return s == s[::-1]
        return True