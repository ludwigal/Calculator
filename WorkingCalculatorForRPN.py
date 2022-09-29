
tokens = ['5', '3', '^', '8', '5', '-', '/', '7', '*']


def evalrpn(tokens):
    stack=[]
    for c in tokens: # Appendar tal tills det kommer en "charachter" och utför då operationen på de två senaste talen, pga polish notation.
        if c == "+":
            #print(stack.pop())
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a, b  = stack.pop(), stack.pop()
            stack.append(b-a)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        elif c == "^":
            x, y = stack.pop(), stack.pop()
            g=y
            for i in range(x-1):
                g=g*y
            stack.append(g)
        else:
            stack.append(int(c))
    return stack[0]

#x = evalrpn(tokens) # Ta bort # för att räkna ut i denna filen endast
#print(x) # Ta bort # för att räkna ut i denna filen endast
