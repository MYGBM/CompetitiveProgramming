class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        new_path = path.split("/")

        for char in new_path:
            if char != ".." and char !="." and char !="//" and char !="":
                stack.append(char)
            elif stack and char == "..":
                stack.pop()
       
        return "/" + "/".join(stack)
    


        