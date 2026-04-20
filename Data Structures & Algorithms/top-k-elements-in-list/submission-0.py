class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            if hashmap.get(n):
                hashmap[n] += 1
            else:
                hashmap[n] = 1
        
        frequent_ele = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        most_frequent_ele = [element[0] for element in frequent_ele]
        return most_frequent_ele[:k]