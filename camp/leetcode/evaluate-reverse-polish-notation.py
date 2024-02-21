class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token!="+" and token !="-" and token!="*" and token !="/":
                stack.append(int(token))
            elif token =="+":
                ans = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(ans)
                
            elif token =="*":
                ans = stack[-1] * stack[-2]
                stack.pop()
                stack.pop()
                stack.append(ans)
                
            elif token =="/":
                ans = int(stack[-2]/stack[-1])
                stack.pop()
                stack.pop()
                stack.append(ans)
                
            elif token =="-":
                ans = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(ans)
                

          

        return stack[-1]
            
            
              
            

        