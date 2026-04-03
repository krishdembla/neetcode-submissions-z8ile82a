class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i,a in enumerate(nums):
            if a > 0:
                break
            
            #same 2 consec elements
            if i > 0 and a == nums[i-1]:
                continue
            
            l,r = i + 1, len(nums) - 1 #initialising left right for 2 pointer approach
            while l < r:
                threeSum = a + nums[l] + nums [r]
                #if sum is larger than 0 we want to decrease right where right most is largest value in sorted list
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res



