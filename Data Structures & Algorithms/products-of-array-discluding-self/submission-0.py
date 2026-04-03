class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod= 1
        zero_counter = 0
        #iterating through nums to get num of zeros and product of non 0 elements
        for num in nums:
            if num:
                prod *= num
            else:
                zero_counter += 1
        if zero_counter > 1: #then the result array is all 0s
            return [0] * len(nums)

        res = [0] * len(nums) #initializing
        for i,c in enumerate(nums):
            if zero_counter:
                res[i] = 0 if c else prod #if c is a valid number, the result will be 0, if c is 0 the result will be prod
            else:
                res[i] = prod // c
        return res



