class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        if n == 0: return 1
        
        total = 1
        add_count = 9

        for i in range(n):
            total += add_count
            add_count *= (9-i)
            
        return total