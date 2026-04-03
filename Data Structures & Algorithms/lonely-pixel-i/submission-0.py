class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        #iterate inside a double for loop while storing a current row/column inside hm
        #inside hm if val of key B is 1
        count = 0
        #hm count for an idx i or j goes up 1 if that row has a 'B'
        rowCount = defaultdict(int)
        colCount = defaultdict(int)
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    rowCount[i] += 1
                    colCount[j] += 1
                else:
                    continue
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B' and rowCount[i] == 1 and colCount[j] == 1:
                    count += 1
        return count
        