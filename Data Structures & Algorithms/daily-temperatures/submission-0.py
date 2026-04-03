class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [] #stack to store decreasing order of temperatures

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # is newly encountered temp > top of stack temp
                prevTemp,prevIdx = stack.pop() #get t,i pair from top of stack
                answer[prevIdx] = i - prevIdx # i - prevIdx gives number of days taken from prevIdx temp to get to warmer temp at i
            stack.append((t,i))
        return answer
        