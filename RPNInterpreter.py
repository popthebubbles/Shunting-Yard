def RPNParser(exp):
    output_stack = []
    while len(exp):
        x = exp.pop(0)
        
        if x == "+" or x == "-" or x == "*" or x == "/" or x == "^":
            b = output_stack.pop()
            a = output_stack.pop()
            output_stack.append(operator_parse(a, b, x))
        else:
            output_stack.append(x)

    return output_stack[0]



def operator_parse(a, b, operator):
    
    a = float(a)
    b = float(b)
    
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    elif operator == "^":
        return a ** b


exp = ['1', '3', '+', '2', '^', '7', '+', '2', '-']
