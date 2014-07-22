import RPNInterpreter

RPNP = RPNInterpreter.RPNParser

def precedence_lookup(token):
    if token == '+':
        return (2, 'left')
    elif token == '-':
        return (2, 'left')
    elif token == '*':
        return (3, 'left')
    elif token == '/':
        return (3, 'left')
    elif token == '^':
        return (4, 'right')
    elif token == '(':
        return (0, 'left')
    else:
        return "error"

def shunting_yard(exp):
    #output queue
    q = []
    #operator stack
    stk = []
    while(len(exp) > 0):
        x = exp.pop(0)
        if x == "+" or x == "-" or x == "*" or x == "/" or x == "^":
            #determine precedence and associativity
            ptoken = precedence_lookup(x)
            if len(stk) > 0:
                temp = precedence_lookup(stk[-1])
            
                while (len(stk) > 0 and ptoken[0] <= temp[0] and ptoken[1] == 'left') or (len(stk) > 0 and ptoken[0] < temp[0]):
                    y = stk.pop()
                    q.append(y)

            stk.append(x)

        elif x == '(':
            stk.append(x)
        elif x == ')':
            while not stk[-1] == '(':
                temp = stk.pop()
                q.append(temp)
            stk.pop()
        else:
            q.append(x)
                
    while len(stk) > 0:
        q.append(stk.pop())
    return q

def string_parse(inp):
    exp = []
    for x in range(len(inp)):
        if not inp[x] == ' ':
            exp.append(inp[x])
    return exp


exp = raw_input("Please enter an expression to be evaluated: \n")
exp = string_parse(exp)
exp = shunting_yard(exp)
result = RPNP(exp)
print(result)


