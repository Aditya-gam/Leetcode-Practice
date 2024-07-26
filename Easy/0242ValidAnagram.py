class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
    
    def isAnagram2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        counter = [0] * 26
        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1
        
        for count in counter:
            if count != 0:
                return False
        
        return True
    
    def isAnagram3(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        set_s = set(s)
        set_t = set(t)
        if set_s != set_t:
            return False
        
        for char in set_s:
            if s.count(char) != t.count(char):
                return False
            
        return True