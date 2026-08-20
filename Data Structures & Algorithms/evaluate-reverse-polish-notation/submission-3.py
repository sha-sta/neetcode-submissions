class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            stack.append(tokens[i])
            if stack[-1] == "+" or stack[-1] == "-" or stack[-1] == "*" or stack[-1] == "/":
                operator = stack.pop()
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if operator == "+":
                    stack.append(f"{num1 + num2}")
                elif operator == "-":
                    stack.append(f"{num1 - num2}")
                elif operator == "*":
                    stack.append(f"{num1 * num2}")
                elif operator == "/":
                    stack.append(f"{int(num1 /num2)}")
        return int(stack[0])