class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_characters = []
        for character in s:
            s_characters.append(character)
        
        t_characters = []
        for character in t:
            t_characters.append(character)
        s_characters.sort()
        t_characters.sort()
        return s_characters == t_characters