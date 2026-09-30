class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        twin={
            "}":"{",
            "]":"[",
            ")":"("
        }
        for c in s:
            if c in twin:
                if stack: 
                    if stack[-1]!=twin[c]:
                        return False
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(c)
        return not stack
