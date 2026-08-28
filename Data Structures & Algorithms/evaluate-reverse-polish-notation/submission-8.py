class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                right = stack.pop()
                left = stack.pop()

                match t:
                    case "+":
                        stack.append(left + right)
                    case "-":
                        stack.append(left - right)
                    case "*":
                        stack.append(left * right)
                    case "/":
                        stack.append(int(left / right))

        return stack.pop()
