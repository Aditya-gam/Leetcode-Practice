class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        n = len(chars)

        if n == 0:
            return 0

        i = 0
        j = 0

        while i < n:
            count = 0
            char = chars[i]

            while i < n and chars[i] == char:
                i += 1
                count += 1

            chars[j] = char
            j += 1

            if count > 1:
                for digit in str(count):
                    chars[j] = digit
                    j += 1

        return j
