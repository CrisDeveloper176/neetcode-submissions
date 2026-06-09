class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ')':'('
            ,']':'['
            ,'}':'{'
        }

        for char in s:
            if char in "({[":
                stack.append(char)
            elif char in close_to_open:
                if stack and stack[-1] == close_to_open.get(char):
                    stack.pop()
                else:
                    return False
        return not stack