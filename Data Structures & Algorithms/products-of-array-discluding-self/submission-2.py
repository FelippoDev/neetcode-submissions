import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [0] * length
        postfix = [0] * length
        product = [0] * length

        prefix[0] = postfix[-1] = 1
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = prefix[i] * nums[i]
            else:
                prefix[i] = prefix[i - 1] * nums[i]
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                postfix[i] = postfix[i] * nums[i]
            else: 
                postfix[i] = postfix[i + 1] * nums[i]
        for i in range(len(nums)):
            if i == 0:
                product[i] = postfix[i + 1]
            elif i == len(nums) - 1:
                product[i] = prefix[i - 1]
            else:
                product[i] = prefix[i - 1] * postfix[i + 1]
        return product
            
            