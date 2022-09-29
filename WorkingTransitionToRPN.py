from WorkingCalculatorForRPN import *
operator_dict = {"^": 3,
                 "*": 2,
                 "/": 2,
                 "+": 1,
                 "-": 1,
                 # "(": 0,
                 # ")": 8
                 }
parenthesis_dict = {
    "(": 1,
    ")": 0
}

operator_assoc = {"^": 1,  # right
                  "*": 0,  # left
                  "/": 0,
                  "+": 0,
                  "-": 0,
                  "(": 0,
                  ")": 0,
                  }

test1 = "1-2*(5-(6-7-8))/9"

from time import sleep

current_equation = test1
stack = []
output_queue = []


# if it is an operand we push it to the output queu
def operand_check(element):
    if (element not in operator_dict.keys()) and (element not in parenthesis_dict.keys()):
        output_queue.append(element)


def if_paranthesis(element):
    # push down the left parenthesis
    if element == "(":
        stack.append(element)
    # if it's right parenthesis then pop everything out of stack until
    # you reach left parenthesis
    elif element == ")":
        while stack[-1] != "(":
            temp = stack.pop()
            output_queue.append(temp)
        # to remove left parenthesis
        stack.pop()


def if_operator(element):
    if element in operator_dict.keys():
        while (len(stack) != 0) and if_associative(element) and does_top_of_stack_have_operator():
            temp = stack.pop()
            output_queue.append(temp)
        stack.append(element)


def if_associative(element):
    if stack[-1] == "(" or ((operator_assoc[element] == 0) and (operator_dict[element] <= operator_dict[stack[-1]])):
        return True
    elif stack[-1] == "(" or ((operator_assoc[element] == 1) and (operator_dict[element] < operator_dict[stack[-1]])):
        return True
    else:
        return False


def does_top_of_stack_have_operator():
    return True if stack[-1] in operator_dict.keys() else False


def empty_stack():
    while len(stack) != 0:
        temp = stack.pop()
        output_queue.append(temp)


# main stream
for element in current_equation:
    operand_check(element)

    if_paranthesis(element)

    if_operator(element)

    #print("stack:", stack)
    #print("output queu", output_queu)
    # sleep(0.5)

empty_stack()

print("stack:", stack)
print("output queue", output_queue)
print(" ".join(output_queue))
calc = evalrpn(output_queue) # Ta bort för att räkna ut, måste ha båda filerna i samma mapp
print(calc) # Ta bort för att räkna ut, måste ha båda filerna i samma mapp