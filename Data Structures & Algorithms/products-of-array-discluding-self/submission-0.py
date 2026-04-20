import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        nums_len = len(nums)
        for i in range(nums_len):
            if i == 0:
                products.append(math.prod(nums[i + 1:]))
            elif i == (nums_len - 1):
                products.append(math.prod(nums[:i]))
            else:
                products.append(math.prod(nums[:i] + nums[i + 1:]))
        return products
        

        