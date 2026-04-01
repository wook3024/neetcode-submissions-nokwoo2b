class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        source = dict()
        target = dict()
        for char in s:
            if char in source:
                source[char] += 1
            else:
                source[char] = 1
        for char in t:
            if char in target:
                target[char] += 1
            else:
                target[char] = 1

        if len(source) != len(target):
            return False

        for key, value in source.items():
            if key not in target:
                return False
            if source[key] != target[key]:
                return False
        
        return True

        
    
