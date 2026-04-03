class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        maxx = -1

        #we start iterating from right to left, and keep updating max
        #when we are at i we replace i with max at that current moment (since that max is to the right of i)
        for i in range(len(arr) - 1, -1, -1):
            temp = maxx
            if arr[i] > maxx:
                maxx = arr[i]
            arr[i] = temp
        return arr
        


        