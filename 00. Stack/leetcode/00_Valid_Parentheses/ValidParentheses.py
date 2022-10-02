class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', '}':'{', ']':'['}
        li = []
        
        for bracket in s:
            if bracket in brackets:
                if len(li) == 0:
                    return False
                
                if li.pop() != brackets[bracket]:
                    return False
            else:
                li.append(bracket)
        
        if len(li) == 0: return True