class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p,s in zip(position, speed)] #creating an array of pairs

        stack = []
        for p,s in sorted(pair)[::-1]: #reverse sorted order
            stack.append((target - p)/s) #appending the time that the car will take to reach target
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() #there is an intersection (Fleet) and then we pop the latest added car (Since we are going right to left)
        return len(stack)