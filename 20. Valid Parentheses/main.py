class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ["(", "{", "["]:
                stack.append(i)
            elif not len(stack):
                return False
            elif i in [")", "}", "]"]:
                curr = stack.pop()
                if curr == "(" and i == ")":
                    continue
                if curr == "{" and i == "}":
                    continue
                if curr == "[" and i == "]":
                    continue
                return False
        if len(stack):
            return False
        return False
