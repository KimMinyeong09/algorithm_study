class Solution:
    def longestValidParentheses(self, s: str) -> int:
        li = [-1]
        maxCount = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                li.append(i)
            else:
                li.pop()
                if not li:
                    li.append(i)
                else: 
                    maxCount = max(maxCount, i-li[-1])
        return maxCount