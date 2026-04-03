class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() #costs nlogn
        for i,a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i-1]: #checking second ele onwards to see if it is not the same as the previous
                continue
            
            l = i+1
            r = len(nums)-1

            while l < r:
                threesum = a + nums[l] + nums[r]
                
                if threesum > 0:
                    r-=1
                elif threesum < 0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return res
                

