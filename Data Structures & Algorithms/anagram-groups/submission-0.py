class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            if hashmap.get(str(sorted(s))):
                hashmap[str(sorted(s))].append(s)
            else:
                hashmap[str(sorted(s))] = [s]

        return [anagrams for anagrams in hashmap.values()]