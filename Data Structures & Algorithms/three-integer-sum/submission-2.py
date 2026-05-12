class Solution:
    """[-4, -1, -1, 0, 1, 2]"""
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ordered_nums = sorted(nums)
        answer = []
        for i in range(len(ordered_nums) - 2):
            left = i + 1
            right = len(ordered_nums) - 1
            while left < right:
                res = ordered_nums[left] + ordered_nums[right] + ordered_nums[i]
                if res == 0:
                    if [ordered_nums[left],ordered_nums[right],ordered_nums[i]] in answer:
                        left += 1
                        right -= 1
                    else:
                        answer.append([ordered_nums[left],ordered_nums[right],ordered_nums[i]])
                        left += 1
                        right -= 1
                elif res < 0:
                    left += 1
                else:
                    right -= 1
        return answer