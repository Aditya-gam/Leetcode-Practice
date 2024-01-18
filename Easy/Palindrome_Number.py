class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if isinstance(x, int):
            if str(x) == str(x)[::-1]:
                return True
            return False
        return False
        