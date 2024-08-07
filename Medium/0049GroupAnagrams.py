class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        anagrams = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)

        return anagrams.values()

    def groupAnagrams2(self, strs):

        anagrams = {}
        for s in strs:
            key = tuple(sorted(s))
            anagrams[key] = anagrams.get(key, []) + [s]

        return anagrams.values()
    
    def groupAnagrams3(self, strs):
            
            anagrams = {}
            for s in strs:
                key = tuple(sorted(s))
                anagrams[key] = anagrams.get(key, []) + [s]
    
            return list(anagrams.values())
    
    def groupAnagrams4(self, strs):
                
                anagrams = {}
                for s in strs:
                    key = tuple(sorted(s))
                    anagrams[key] = anagrams.get(key, []) + [s]
        
                return [group for group in anagrams.values()]