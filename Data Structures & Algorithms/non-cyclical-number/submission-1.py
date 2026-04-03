class Solution:
    def isHappy(self, n: int) -> bool:
        #need a helper function to do the recursive digit squaring math
        #then based on that result find out if a happy number or not
        if n == 1:
            return True
        
        def square_sum(n: int) -> bool:
            # if n == 1:
            #     return True
            # else:
            #     return ((n % 10) ** 2) + non_cyclical(math.floor(n/10))
            sum = 0
            while n != 0:
                sum += (n % 10) ** 2 #square the digit
                n = math.floor(n/10)
            return sum

        num_set = set()
        while n != 1:
            n = square_sum(n)
            if n in num_set:
                return False
            else:
                num_set.add(n)
        return True
        
        
        


