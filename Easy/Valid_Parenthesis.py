class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Create a stack
        stack = []

        # Create a dictionary of valid parenthesis
        valid_parenthesis = {')':'(', '}':'{', ']':'['}

        # Iterate through the string
        for char in s:
            # If the char is in the valid parenthesis dictionary
            if char in valid_parenthesis:
                # If the stack is empty, return False
                if not stack:
                    return False
                # If the top of the stack is not the valid parenthesis, return False
                if stack.pop() != valid_parenthesis[char]:
                    return False
            # Else, append the char to the stack
            else:
                stack.append(char)

        # If the stack is empty, return True
        if not stack:
            return True
        return False