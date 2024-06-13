def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def is_operator(c):
        return c in precedence

    def is_operand(c):
        return c.isalnum()

    stack = []
    output = []

    for char in expression:
        if is_operand(char):
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop() 
        elif is_operator(char):
            while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[char]:
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(output)


expression = "a+b*(c-d)"
postfix_expression = infix_to_postfix(expression)
print(postfix_expression)
