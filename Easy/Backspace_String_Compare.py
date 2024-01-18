class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        stack_s = []
        stack_t = []
        for i in s:
            if i == '#':
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(i)

        for i in t:
            if i == '#':
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(i)

        return stack_s == stack_t