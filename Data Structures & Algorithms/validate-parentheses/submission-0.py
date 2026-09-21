class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s:
            if stack != []:
                if i == ')':
                    if stack[len(stack)-1] == '(':
                        stack.pop()
                        continue
                elif i == '}':
                    if stack[len(stack)-1] == '{':
                        stack.pop()
                        continue
                elif i == ']':
                    if stack[len(stack)-1] == '[':
                        stack.pop()
                        continue
            stack.append(i)
        if stack != []:
            return False
        else:
            return True
        