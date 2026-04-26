class Solution:
    """[-4, -1, -1, 0, 1, 2]"""
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    triplet = [nums[i], nums[left], nums[right]]
                    if triplet in triplets:
                        left += 1
                        right -= 1
                    else:
                        triplets.append(triplet)
                        left += 1
                        right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        return triplets