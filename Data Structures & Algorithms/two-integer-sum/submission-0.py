class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            try:
                second_sum = nums.index(target - nums[i], i + 1)
                break
            except ValueError as e:
                continue
        return [i, second_sum]
