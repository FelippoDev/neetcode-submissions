class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_characters = [char for char in s]
        t_characters = [char for char in t]
        s_characters.sort()
        t_characters.sort()
        return s_characters == t_characters