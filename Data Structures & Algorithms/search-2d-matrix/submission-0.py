class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix), len(matrix[0])
        top, bot = 0, r-1
        while top<=bot:
            mid = (top + bot)//2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break
        
        if not (top <= bot):
            return False
        row = (top + bot)//2
        left,right = 0,c-1
        while left <= right:
            m = (left + right)//2
            if target > matrix[row][m]:
                left = m + 1
            elif target < matrix[row][m]:
                right = m - 1
            else:
                return True
        return False