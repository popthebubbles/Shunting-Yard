#RPNParser takes a list of tokens in Reverse Polish Notation and evaluates it
def RPNParser(exp):
    #The output stack
    stk = []
    while len(exp):
        x = exp.pop(0)
        
        if x == "+" or x == "-" or x == "*" or x == "/" or x == "^":
            b = stk.pop()
            a = stk.pop()
            stk.append(operator_parse(a, b, x))
        else:
            stk.append(x)

    return stk[0]



def operator_parse(a, b, operator):
    
    #convert the input from strings to floats
    a = float(a)
    b = float(b)
    
    #perform the operation
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

#Can be used to test/see the Parser in action
#exp = ['4', '6', '4', '2', '^', '7', '*', '-', '4', '^', '*']

#print(RPNParser(exp))
