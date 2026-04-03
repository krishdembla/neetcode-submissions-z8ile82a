class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i in range(len(nums)):
            hm[nums[i]] = i
        
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hm.keys() and i != hm[difference]: #if the rem value is in hm and the index of current and difference is not the same
                return [i, hm[difference]]
            else:
                continue
        
        return []

        



