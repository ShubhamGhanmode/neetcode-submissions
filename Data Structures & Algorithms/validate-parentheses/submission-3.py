class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s:
            if stack != []:
                last_item = stack[len(stack)-1]
                if i == ')':
                    if last_item == '(':
                        stack.pop()
                        continue
                elif i == '}':
                    if last_item == '{':
                        stack.pop()
                        continue
                elif i == ']':
                    if last_item == '[':
                        stack.pop()
                        continue
            stack.append(i)
        if stack != []:
            return False
        else:
            return True
        