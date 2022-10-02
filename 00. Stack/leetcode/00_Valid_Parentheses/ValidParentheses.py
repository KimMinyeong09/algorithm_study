class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', '}':'{', ']':'['}
        li = []
        
        for bracket in s:
            if bracket in list(brackets.values()):
                li.append(bracket)
            elif bracket in list(brackets.keys()):
                if len(li) == 0:
                    return False
                if li.pop() != brackets[bracket]:
                    return False
        if len(li) == 0:
            return True