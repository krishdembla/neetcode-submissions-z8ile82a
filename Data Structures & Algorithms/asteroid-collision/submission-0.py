class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #we can use a stack and compare with element in asteroids and then choose which survives and append it to the stack
        stack = []
        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:  # collision condition
                if abs(ast) > stack[-1]:      # ast wins
                    stack.pop()
                elif abs(ast) < stack[-1]:    # stack wins
                    break
                else:                          # both die
                    stack.pop()
                    break
            else:
                stack.append(ast)
        return stack