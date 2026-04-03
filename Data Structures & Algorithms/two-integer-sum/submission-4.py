class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            hm[nums[i]] = i

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hm.keys() and i != hm[difference]:
                return [i, hm[difference]]
            else:
                continue

        return []