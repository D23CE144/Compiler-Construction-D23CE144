import re
import operator

def evaluate_expression(expression):
    try:
        tokens = re.findall(r'\d+\.?\d*|[()+\-*/^]', expression)
        output_queue = []
        operator_stack = []
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        associativity = {'+': 'L', '-': 'L', '*': 'L', '/': 'L', '^': 'R'}
        
        for token in tokens:
            if re.match(r'\d+\.?\d*', token):
                output_queue.append(float(token))
            elif token in precedence:
                while (operator_stack and operator_stack[-1] in precedence and
                       ((associativity[token] == 'L' and precedence[token] <= precedence[operator_stack[-1]]) or
                        (associativity[token] == 'R' and precedence[token] < precedence[operator_stack[-1]]))):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()
                else:
                    return "Invalid expression"
        
        while operator_stack:
            if operator_stack[-1] in '()':
                return "Invalid expression"
            output_queue.append(operator_stack.pop())
        
        return evaluate_rpn(output_queue)
    except Exception:
        return "Invalid expression"

def evaluate_rpn(rpn_queue):
    stack = []
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '^': operator.pow}
    
    for token in rpn_queue:
        if isinstance(token, float):
            stack.append(token)
        elif token in operators:
            if len(stack) < 2:
                return "Invalid expression"
            b, a = stack.pop(), stack.pop()
            stack.append(operators[token](a, b))
        else:
            return "Invalid expression"
    
    return stack[0] if len(stack) == 1 else "Invalid expression"

# Take input from user
expression = input("Enter an arithmetic expression: ")
result = evaluate_expression(expression)
print("Result:", result)
