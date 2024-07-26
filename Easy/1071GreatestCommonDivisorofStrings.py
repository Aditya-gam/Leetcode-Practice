class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        if str1 + str2 != str2 + str1:
            return ''

        if str1 == str2:
            return str1

        return str1[:self.gcd(len(str1), len(str2))]

    def gcd(self, a, b):
        while b:
            a, b = b, a % b

        return a

    def gcdOfStrings2(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        if str1 + str2 != str2 + str1:
            return ''

        return str1[:self.gcd2(len(str1), len(str2))]

    def gcd2(self, a, b):
        if b == 0:
            return a

        return self.gcd2(b, a % b)

git commit -m "Easy 1071. Greatest Common Divisor of Strings"