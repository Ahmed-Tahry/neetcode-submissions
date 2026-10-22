class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack_inv = []
        if s[0] == ")" or s[0] == "]" or s[0] == "}":
            return False
        for i in s :
            if i == "["  :
                stack.append("]")
            if i == "("  :
                stack.append(")")
                
            if i == "{"  :
                stack.append("}")
                               
            if len(stack) >=1 :
                if i == stack[-1] :
                    stack.pop()
        for i in reversed(s):
            if i == "]"  :
                stack_inv.append("[")
            if i == ")"  :
                stack_inv.append("(")
                
            if i == "}"  :
                stack_inv.append("{")
                               
            if len(stack_inv) >=1 :
                if i == stack_inv[-1] :
                    stack_inv.pop()
        if len(stack) == 0 and len(stack_inv) ==0 :
            return True
        else : 
            return False
        



        