class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {} # storage is O(n) only one hm made 
        for i,j in enumerate(nums):
             hm[j] = i #storing the index with corresponding val as key
            
        for i,n in enumerate(nums):
            difference = target - n
            if difference in hm and hm[difference] != i:
                return[i, hm[difference]]
           


            
        