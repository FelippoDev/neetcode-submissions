from collections import Counter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            if (target - num) in nums:
                try:
                    second_idx = nums.index(target - num, idx + 1)
                    break
                except:
                    print(idx + 1)
        return [idx, second_idx]
