class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] != ")" and s[i] != "]" and s[i]!="}":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                else:
                    if s[i] == ")":
                        if stack[-1] != "(":
                            return False
                        else:
                            stack.pop()
                    elif s[i] =="]":
                        if  stack[-1] != "[":
                            return False
                        else:
                            stack.pop()
                    elif  s[i] =="}":
                        if stack[-1] != "{":
                            return False
                        else:
                            stack.pop()
        else:
            if stack:
                return False
            else:
                return True
                



        