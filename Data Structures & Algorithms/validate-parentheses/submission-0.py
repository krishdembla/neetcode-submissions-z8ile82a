class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #initialising a dict with key value pair as the open and close brackets
        bracket_set = {")" : "(", "]" : "[", "}" : "{"}
        for ch in s:
            if ch in bracket_set:
                #checking if the bottom of stack = value of that bracket in dict
                if stack and stack[-1] == bracket_set[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return True if not stack else False
        