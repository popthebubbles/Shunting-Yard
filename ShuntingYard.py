import RPNInterpreter
import re

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
    num = None
    for x in inp:
        if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9':
            if num == None:
                num = x
            else:
                num = num + x
        elif x == ' ':
            if not num == None:
                exp.append(num)
                num = None
        else:
            if num == None:
                exp.append(x)
            else:
                exp.append(num)
                exp.append(x)
                num = None

    if not num == None:
        exp.append(num)
    return exp
exp = raw_input("Please enter an expression to be evaluated: \n")
exp = string_parse(exp)
exp = shunting_yard(exp)
result = RPNP(exp)
print(result)


