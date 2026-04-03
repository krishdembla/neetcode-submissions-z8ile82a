class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        return sum(sorted(self.scores.values(), reverse = True)[:K]) #takes O(nlogn)
        # res = 0
        # for i in range(K):
        #     res += sorted_scores[i]
        # return res
            

    def reset(self, playerId: int) -> None:
        del self.scores[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
